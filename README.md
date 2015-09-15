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

    python2.7 SigVanity.py 1BTE

will search for a Bitcoin address starting with "1BTZ"

    python2.7 SigVanity.py 3BTE (not yet implemented)

will search for a P2SH address starting with "3BTE", and will give out 3 Bitcoin standard addresses.


Random source for key generation :

* CryptGenRandom in Windows
* /dev/urandom   in Unix-like


First version without any P2SH capabilities, only works with standard Bitcoin "1xxx" "addresses.


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
