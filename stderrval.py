#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np

from errval import *
from errvallist import *

'''
Convenience functions in order to get standard errors.

The standard error (ste; here designated as \Delta)
 \Delta = \frac{1}{\sqrt{n}} \sqrt{\frac{1}{n-1} \sum\limits_{i=0}^{n-1} (x_i - \bar{x})^2}
is NOT the same as the standard deviation (std; designated as \sigma)!
Basically, it is
\Delta = 1/sqrt(n) * \sigma.
However, be careful:
For the standard deviation (std) we use the
*unbiased* estimate of the standard deviation.

The std requires the mean of a distribution;
it is the average square difference of the data points
to this mean.
In reality, this mean (\mu) is fix.
But, unfortunately for us,
we don't know it (usually).
Instead, we have to revert to an estimate (\bar{x}),
 \mu \neq \bar{x}.

Because we estimate the mean with the given data
 \bar{x} = \frac{1}{n} \sum\limits_{i=0}^{n-1} x_i,
we lose one degree of freedom for estimating std:
 \sigma = \sqrt{\frac{1}{n-1} \sum\limits_{i=0}^{n-1} (x_i - \bar{x})^2}
(mind the n-1 in the denomintor!).
Without this n-1, the estimate would be biased.
Note, this bias deminishes as n is big:
 1/n \approx 1/(n-1),
for n>>1.
Non the less, it is important as the meaning --
from a mathematical point of view -- 
changes.


With all this said,
it is necessary to know the difference between using
a value +- std versus value +- ste:

The standard deviation (std; \sigma)
tells you how widly spread your measurements are.
A measurement yields a probabilistic value
corresponding to its underlying probability distribution.
Consequentially, it is fixed;
it doesn't change the more data points you gather.
(if you don't know any better,
it's probably a Gaussian distribution...)
and the std tells you about this distribution.
(In practice the value of \sigma changes,
but that's because \sigma tells you an estimate
of the real deviation, and this estimate
gets more accurate the more information you provide it.
But the underlying deviation is fix.)

The standard error, on the other hand,
tells you about how good your knowledge
of the true value is.
Again, your measurement will give you different values.
These are spread according to a specific distribution.
But the thing that you measure
does not change, it stays the same thing
(ok, this depends on how you measure...).
With repeated measurements the average of these results
converge towards this true value.
And that's what you actualy want to know about.
You want to report a value +- how sure you are about this value.

'''


def stderrval(li):
    # errval with standard error from a list
    # standard error being the unbiased std divided by n
    return errval(np.mean(li),\
                   1.0/np.sqrt(len(li))*np.std(li,ddof=1))


#---------------------------------------------------------------------------------------



def stderrvallist(li):
    # errvallist with standard errors from a n-dim list
    # standard error being the unbiased std divided by n
    # input li = [[1,2,3],
    #             [2,3,4]]
    # outp res = [1.5+-0.5,2.5+-0.5,3.5+-0.5]
    return errvallist(np.mean(li,axis=0),\
                       1.0/np.sqrt(len(li))*np.std(li,axis=0,ddof=1))



