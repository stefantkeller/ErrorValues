errorvalues
===========

TL;DR -- too lazy to keep track of error propagation? Use this.  


Working with data that have errors attached can be tedious.
Natural reaction by everyone: ignore them.  
This module allows you to
combine value and error in one and the same object;
an `errval`.
Subsequentially,
you can perform calculations with this object
like with regular numbers.
The error propagation is carried out automatically.  

If you have a list of `errval`s --
an `errvallist` --
you can manipulate these data
as used to, from `numpy.array`s.
See the examples below.  

The resulting `errval`s are meant
to be copied from the command line,
or used in a LaTeX environment.
For this there are several options
what the '+-' sign between
value and error
should be.
Again, see the examples below.  

Caveat:  
The implemented operations are carried out as they are supposed to do.
However, you as a user still have to judge whether what YOU do makes sense.
If you work with power readings from a laser,
these values will be `>=0`;
because physics!
None the less, you may get a result like `2+-3 W`.
This error suggests the value might be negative.
This is nonsense.
Mathematically, this result is fine.
In other applications (where negative values are allowed), this result is fine.
But in a power reading not.  
You are responsible for the statistical implications of your analysis.
This library can take off the burden
to keep track of the uncertainties attached to values.
But it cannot think for you!  


Examples:


import errorvalues as ev  

a = ev.errval(2,3) # value 2, with error 3  
b = ev.errval(3,4)  
print a+b # 5 \pm 5  

Modify output behavior  
d = ev.errval(6,1,'+-')  
print d # 6 +- 1, if you're not used to read \pm  
e = ev.errval(7,2,'cp')  
print e # errval(7,2)  
f = ev.errval(8,3,'cpp')  
print f # errval(8,3,errvalmode)  
The latter two options are particularly useful
in order to save the output in a file.
Text with `errval()` can be converted into actual `errval`s:  
g = ev.str2errvallist('errval(2,3)+errval(3,4)')
print g # [2.0 \pm 3.0,3.0 \pm 4.0]

Work with lists  

Some advanced functions  
wmean  
linreg  
max, min  
interp  

