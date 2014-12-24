"""
https://github.com/stefantkeller/ErrorValues

Convenience class to work with error (aka uncertainty) attached

It is
c = f(a+-da,b+-db)
=> dc = sqrt( (df/da)**2 * da**2 + (df/db)**2 * db**2 )

each implemented operation {+, -, *, /, **, abs()} returns a new instance.
"""
