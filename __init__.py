"""
https://github.com/stefantkeller/ErrorValues

Convenience class to work with error (aka uncertainty) attached

It is
c = f(a+-da,b+-db)
=> dc = sqrt( (df/da)**2 * da**2 + (df/db)**2 * db**2 )

each implemented operation {+, -, *, /, **, abs()} returns a new instance.
"""

__author__ = "Stefan T. Keller"
__version__ = '1.0'


import errval
from errval import *

import errvallist
from errvallist import *

import stderrval
from stderrval import *

import functions
from functions import *

#__all__ = ['errval','errvallist','stderrval','functions']
