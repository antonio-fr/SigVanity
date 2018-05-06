  SigVanity
===========

SigVanity is a P2SH address wallet generator fully written in python.

* Pure Python code
* Cross-platform code
* No-dependencies
* Generate address the easiest way


## Using SigVanity

You need Python 2.7 (not tested on 3.x).

Launch SigVanity.py without any args to generate a single wallet address.

You can enter an optional argument, the argument must be a FirstBits address like 1xxx or 3xxx to start a vanity generation.

For "3xxx" P2SH addresses, you need to add number of keys required and total number or keys.

Using P2SH, you can optionally input PubKeys 


    SigVanity.py [ <1xFirstBits>          |
                    m <KeysReq> <KeysTot> |
                   <3xFirstBits> <KeysReq> <KeysTot> [<PubKeyHex> [<PubKeyHex> ...]] ]



## Examples:

Generate a standard Bitcoin address

    SigVanity.py

Generate a Multisig 2-to-3 Bitcoin address

    SigVanity.py m 2 3

Search for a Bitcoin address starting with "1BTE"

    SigVanity.py 1BTE

Search for a 2-to-3 P2SH address starting with "3BTE", give out 3 Bitcoin standard addresses.

    SigVanity.py 3BTE 2 3 

Then you can add public keys to search for a Multisig Bitcoin address, with one or more key given

    SigVanity.py m 2 3 0407a730a52979a57f4dc659c4c75ff6c24e844abcdefxyz


    >SigVanity.py 3AB 3 4 0492EBE75FEEFFD857DA28A7644CC04B6CE07BAF4D1CFD19DBD1A5D901C49D6A5D359E636F45226878FC1E5A14921329CA25876705D7A1225CB33BBAEB4E38BDDA

    Generate new Bitcoin address from random or vanity (FirstBits)

    Vanity Mode, please Wait ...
    Press CTRL+C to stop searching
    Found!
    Search Speed :  72.8147449588  per second


    Address :  3ABm2y2MUnZukHUAxgcQDK4pnR6z7eTzmK

    P2SH : 3 required over 4 keys

    Key #1
    PrivKey 1:  5KDjdNQFFRBmCDnyQ9hXxhSWcZEQdvsGHg6a6KhgRdJ8xnKkm7j
    Related Address 1:  17SaVFxZdWFvfU5Lvxegiio1iQ11e6VGgN
    PubKey 1:  0466577128bc6f8771d100b8e2ecdb3eddc257cdc7474656e231a57f55ed114b50ad260cd033c6324fe12863bc7cdb86ecbb578356698cbc919d021958c07c7813

    Key #2
    PrivKey 2:  5HzfijeQjMT6iSiRtuDkXq3AJBgACJeBBi2HHeV3vFkHWr62Lta
    Related Address 2:  1JCKFidoywsTW4EEAYov2KjWAxuk8iTGKw
    PubKey 2:  04f0aba95af6746a03d5b63868d0fa8a87189257f39eb4a686a4dc6f5426adcfe8691a75d31e7c3dae38fdc14656e9218e55e9be7eb7902f12f3e9c4e9228e6b13

    Key #3
    PrivKey 3:  5HxbKVbQv8RLMZ8fMyerUhkBGe3pp6TQRrwZTqFGMhtjonksw6p
    Related Address 3:  12gpZGdyAutjSkrDUBiT2aFDu5FBUguFx5
    PubKey 3:  04ee036092da4b0c8b4ce0d785997a8796a6b6d3d98efd2b353b082388b68300cd8473fbeff940ac0487343c0c555c60724da9dd9f936998d43ad9e7e5708c12f7

    Key #4
    No Private Key for this address, PubKey given
    Related Address 4:  1PYTRkw62rtPuKnohpTNcRSEgQw3darc4d
    PubKey 4:  0492ebe75feeffd857da28a7644cc04b6ce07baf4d1cfd19dbd1a5d901c49d6a5d359e636f45226878fc1e5a14921329ca25876705d7a1225cb33bbaeb4e38bdda



Some code files come from pybitcointools from VButerin

Copyright (c) 2013 Vitalik Buterin


Random source for key generation initialization:

* CryptGenRandom in Windows
* /dev/urandom   in Unix-like


## To Do

* Use pybitcointools for standard address generation


Licence :
----------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
