  SigVanity
===========

SigVanity is a P2SH address wallet generator fully written in python.

* Pure Python code
* Cross-platform code
* Generate address the easiest way


## Using SigVanity

You need Python 2.7 (not tested on 3.x).

Install coincurve

    pip install coincurve

Coincurve is a bindings for libsecp256k1, the heavily optimized C library written by P. Wuille used by Bitcoin core nodes. This new SigVanity version with coincurve, is 400x faster for single addresses and 20x faster for MultiSig.

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


Running example :

    >SigVanity2.py 3ABC 3 4 0492EBE75FEEFFD857DA28A7644CC04B6CE07BAF4D1CFD19DBD1A5D901C49D6A5D359E636F45226878FC1E5A14921329CA25876705D7A1225CB33BBAEB4E38BDDA
    
    Generate new Bitcoin address from random or vanity (FirstBits)
    
    Vanity Mode, please Wait ...
    Press CTRL+C to stop searching
    Found!
    Search Speed :  14733.8131013  per second
    
    
    Address :  3ABCcMiWjCHZb2cCQL4XCNQtgLXDwSmchB
    
    P2SH : 3 required over 4 keys
    
    Key #1
    PrivKey 1:  5J9Haiypxpm2T8rYNCfeN8dfgSd7iTyXsWG9t2xvMuYPguB8VBz
    Related Address 1:  124GRLYUvwVvKuXyDzXEHTiJTWnc4WFrVE
    PubKey 1:  043d6943b4b0cf0f359cb1936b873027e980a2d0287d33c9eef1db007650caee27b83b3f2e2670042e0d7fb3ded6fc647bf0b176897750f548e4310fd5b419f911
    
    Key #2
    PrivKey 2:  5J4YnKFAYkCQCG7a2puGsa73CAAr6P2yUE82Xj5PdM9FX84J4YP
    Related Address 2:  1NGAnqmDF3Mo9bXEAvLDfHzjUTobphzpwV
    PubKey 2:  04d8c24ea73a327a248667354167007c839d603cefde367696c59ec7a5d75a9d5557d30aa7dda73b3648a6d0421adeec8f325e1501e97c33b011599439a4d4bfdc
    
    Key #3
    PrivKey 3:  5KF49ssdSHLZvu6urnxHLEoMqR7QUM9Wsmgm5bZREhDeeuDKaiY
    Related Address 3:  1DcuabC1crJyamLjfGXeY2areG7CTv6rkx
    PubKey 3:  04277ab40f0498505acd0ab087dbc7e473bfcb86cd30d11725d3a66d4fb1d3a5b3195dfe75761eea4dc6192458a74e2af1990ad6a8eb915c9a03a0a53cae8706c5
    
    Key #4
    No Private Key for this address, PubKey given
    Related Address 4:  1PYTRkw62rtPuKnohpTNcRSEgQw3darc4d
    PubKey 4:  0492ebe75feeffd857da28a7644cc04b6ce07baf4d1cfd19dbd1a5d901c49d6a5d359e636f45226878fc1e5a14921329ca25876705d7a1225cb33bbaeb4e38bdda
    


Some code files come from pybitcointools from VButerin

Copyright (c) 2013 Vitalik Buterin


Random source for key generation initialization:

* CryptGenRandom in Windows
* /dev/urandom   in Unix-like


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
