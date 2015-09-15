#!/usr/bin/env python
# coding=utf8

# SigVanity : Bitcoin MultiSig Address Generator
# Copyright (C) 2015  Antoine FERRON
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
# Enter optional argument : a string shorter than 11 chars
#
from lib.ECDSA_BTC import *

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
		cand=hashrand(1024)
		candint=int(cand,16)
	return candint

def compute_adr(priv_num):
	try:
		pubkey = Public_key( generator_256, mulG(priv_num) )
		return pub_hex_base58(pubkey.point.x(),pubkey.point.y())
	except KeyboardInterrupt:
		return "x"

if __name__ == '__main__':
	import multiprocessing
	p = multiprocessing.Pool(int(multiprocessing.cpu_count()))
	import hashlib
	import re
	import sys
	import time
	import os.path
	print "\nGenerate new Bitcoin address from random or vanity (FirstBits)"
	vanity = False
	try:
		if len(sys.argv) > 1:
			arg1 = sys.argv[1]
			assert re.match(r"^[1][a-km-zA-HJ-NP-Z1-9]{1,11}$",arg1) != None
			searchstring = arg1
			listwide=64*int(multiprocessing.cpu_count())
			print searchstring
			vanity = True
	except:
		raise ValueError("Error in argument, not a valid FirstBits string")
	load_gtable('lib/G_Table')
	privkeynum = randomforkey()
	address = compute_adr(privkeynum)
	foundprivkeynum = privkeynum
	if vanity:
		address = None
		newprivkeynum = privkeynum
		print "\nVanity Mode, please Wait ..."
		print "Press CTRL+C to stop searching"
		startTime = time.time()
		try:
			while address == None:
				privkeynumlist = range(newprivkeynum,newprivkeynum+listwide)
				newprivkeynum = newprivkeynum + listwide
				addresslist = p.map(compute_adr,privkeynumlist)
				for index, addressk in enumerate(addresslist, start=0):
					if addressk.startswith(searchstring):
						address = addressk
						foundprivkeynum = privkeynumlist[index]
			print "Found!"
		except KeyboardInterrupt:
			p.terminate()
			print "Interrupted, nothing found\n"
			inter=1
		print "Search Speed : ",(newprivkeynum-privkeynum)/(time.time() - startTime), " per second\n"
	if 'inter' not in locals():
		assert compute_adr(foundprivkeynum) == address
		print "\nAddress :  %s \n" % address
		pvhex = priv_hex_base58(foundprivkeynum)
		print "PrivKey :  %s\n" % pvhex