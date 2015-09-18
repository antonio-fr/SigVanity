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

You can enter an optional argument, the argument must be a FirstBits address like 1xxx or 3xxx


Example:

    python2.7 SigVanity.py

will generate a standard Bitcoin address

    python2.7 SigVanity.py m

will generate a Multisig 2-to-3 Bitcoin address

    python2.7 SigVanity.py 1BTE

will search for a Bitcoin address starting with "1BTZ"

    python2.7 SigVanity.py 3BTE

will search for a 2-to-3 P2SH address starting with "3BTE", and will give out 3 Bitcoin standard addresses.

Then you can add public key (up to 2):

    python2.7 SigVanity.py m 0407a730a52979a57f4dc659c4c75ff6c24e844abcdefxyz

will search for a Multisig 2-to-3 Bitcoin address, with one key given


Some code files come from pybitcointools from VButerin

Copyright (c) 2013 Vitalik Buterin


Random source for key generation initialization:

* CryptGenRandom in Windows
* /dev/urandom   in Unix-like


## To Do

* Add argument handling to choose number of keys
* Print keys addresses
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
