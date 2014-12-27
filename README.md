ErrorValues
===========

Work conveniently with errorbars on your data:  value +- error

Working with data that have errors attached can be tedious; and hence everyone leaves them away.
Not anymore.
Combine the error to the value in one and the same object.
Example:

import ErrorValues as ev

a = ev.errval(2,1) # 2+-1
b = ev.errval(3,1.5)
c = a+b # 5+-1.80277563773
