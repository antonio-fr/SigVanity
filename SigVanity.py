#!/usr/bin/env python2
# coding=utf8

# SigVanity : Bitcoin MultiSig Address Generator
# Copyright (C) 2015-2018  Antoine FERRON
#
# Pure Python address generator with Vanity capabilities
#
# Random source for key generation :
# CryptGenRandom in Windows
# /dev/urandom   in Unix-like
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#
from lib import B58
import coincurve
import bitcoin

def hashrand(num):
	#return sha256 of num times 256bits random data
	rng_data=''
	for idat in xrange(num):
		rng_data = rng_data + os.urandom(32)
	assert len(rng_data) == num*32
	return hashlib.sha256(rng_data).hexdigest()

def randomforkey():
	candint = 0
	r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141L
	while candint<1 or candint>=r:
		candint = int(hashrand(1024),16)
	return candint

def compute_adr(priv_num):
	try:
		pubkey = coincurve.PrivateKey.from_int(priv_num).public_key
		px,py = pubkey.point()
		return B58.pub_hex_base58(px,py)
	except:
		return "x"

def compute_adr_P2SH(args):
	try:
		( priv_num, pubs, nkr, nkt ) = args
		pub = coincurve.PrivateKey.from_int(priv_num).public_key.format(False).encode('hex')
		mscript = bitcoin.mk_multisig_script([pub]+pubs[1:], nkr, nkt)
		return bitcoin.p2sh_scriptaddr(mscript)
	except:
		return "x"

if __name__ == '__main__':
	import multiprocessing
	ncpus = int(multiprocessing.cpu_count())
	p = multiprocessing.Pool(ncpus)
	import hashlib
	import re
	import sys
	import time
	import os.path
	print "\nGenerate new Bitcoin address from random or vanity (FirstBits)"
	vanity = False
	P2SH = False
	try:
		if len(sys.argv) > 1:
			arg1 = sys.argv[1]
			if (re.match(r"^[13][a-km-zA-HJ-NP-Z1-9]{1,10}$",arg1) != None):
				searchstring = arg1
				listwide = ncpus << 8
				vanity = True
				P2SH = searchstring[0]=="3"
			else:
				assert arg1 == "m"
				P2SH = True
			if P2SH == True:
				nkeysneeded = int(sys.argv[2])
				nkeystotal = int(sys.argv[3])
				assert nkeysneeded <= nkeystotal
				rawpubinputlist = sys.argv[4:]
				npubinput = len(rawpubinputlist)
				assert npubinput < nkeystotal
	except:
		raise ValueError("Error in arguments\n\nUse :     SigVanity.py [ <1xFirstBits> |\n  m <KeysReq> <KeysTot> | \
			\n  <3xFirstBits> <KeysReq> <KeysTot> [<PubKeyHex> [<PubKeyHex> ...]]\n]")
	if P2SH:
		privs = [randomforkey() for x in range(nkeystotal-npubinput)]
		pubs = [bitcoin.privtopub(B58.hexa(priv)) for priv in privs]
		pubinputlist = []
		for item in rawpubinputlist:
			pubinputlist.append(item.lower())
		pubs = pubs + pubinputlist
		addresses = [bitcoin.pubtoaddr(pub) for pub in pubs]
		mscript = bitcoin.mk_multisig_script(pubs, nkeysneeded, nkeystotal)
		address = bitcoin.p2sh_scriptaddr(mscript)
		foundprivkeynum = privs[0]
	else:
		privkeynum = randomforkey()
		address = compute_adr(privkeynum)
		foundprivkeynum = privkeynum
	if vanity:
		address = None
		if P2SH:
			newprivkeynum = privs[0]
			print "\nVanity Mode, please Wait ..."
			print "Press CTRL+C to stop searching"
			nstart = privs[0]
			startTime = time.time()
			try:
				while address == None:
					privkeynumlist = range(newprivkeynum, newprivkeynum + listwide)
					newprivkeynum = newprivkeynum + listwide
					addresslist = p.map(compute_adr_P2SH,[(privkeynumu, pubs, nkeysneeded, nkeystotal) for privkeynumu in privkeynumlist])
					addrlf = filter(lambda addri:addri.startswith(searchstring), addresslist)
					if len(addrlf)>0:
						address = addrlf[0]
						foundprivkeynum = privkeynumlist[addresslist.index(address)]
				print "Found!"
			except KeyboardInterrupt:
				p.terminate()
				print "Interrupted, nothing found\n"
				inter=1
		else:
			newprivkeynum = privkeynum
			print "\nVanity Mode, please Wait ..."
			print "Press CTRL+C to stop searching"
			nstart = privkeynum
			startTime = time.time()
			try:
				while address == None:
					privkeynumlist = range(newprivkeynum, newprivkeynum + listwide)
					newprivkeynum += listwide
					addresslist = p.map(compute_adr, privkeynumlist)
					addrlf = filter(lambda addri:addri.startswith(searchstring), addresslist)
					if len(addrlf)>0:
						address = addrlf[0]
						foundprivkeynum = privkeynumlist[addresslist.index(address)]
				print "Found!"
			except KeyboardInterrupt:
				p.terminate()
				print "Interrupted, nothing found\n"
				inter = 1
		print "Search Speed : ",(newprivkeynum-nstart)/(time.time() - startTime), " per second\n"
	if 'inter' not in locals():
		print "\nAddress :  %s \n" % address
		if P2SH:
			print "P2SH : %i required over %i keys\n" % (nkeysneeded,nkeystotal)
			pubs[0] = bitcoin.privkey_to_pubkey(B58.hexa(foundprivkeynum))
			privs[0] = foundprivkeynum
			mscript_test = bitcoin.mk_multisig_script(pubs, nkeysneeded, nkeystotal)
			assert address == bitcoin.p2sh_scriptaddr(mscript_test)
			for x in range(nkeystotal-npubinput):
				print "Key #%i" % (x+1)
				print "PrivKey %i:  %s" % (x+1,B58.priv_hex_base58(privs[x]))
				print "Related Address %i:  %s" % (x+1,bitcoin.pubkey_to_address(pubs[x]))
				print "PubKey %i:  %s\n" % (x+1,bitcoin.privkey_to_pubkey(B58.hexa(privs[x])))
			for x in range(nkeystotal-npubinput,nkeystotal):
				print "Key #%i\nNo Private Key for this address, PubKey given\nRelated Address %i:  %s"\
					% (x+1,x+1,bitcoin.pubkey_to_address(pubs[x]))
				print "PubKey %i:  %s\n" % (x+1,pubs[x])
		else:
			print "PrivKey :  %s\n" % B58.priv_hex_base58(foundprivkeynum)
