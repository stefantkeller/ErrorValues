#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

#from sys import exit

from errval import *
from errvallist import *
from stderrval import *
from functions import *

'''
TODO: actual unittest!
'''



def main():
#    z = errval(0,-1)
    aa, da = 1, 3
    a = errval(aa, da)
    bb, db = 2, 4
    b = errval(bb, db, '+-')
    cc, dc = -3, 5
    c = errval(cc,dc)
    # test basic output functionality
    print 'exp: {0} {1} \ngot: {2} {3}\n---'.format(aa,da, a.val(), a.err())
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(aa,da,a)
    print 'exp: {0} +- {1} \ngot: {2}\n---'.format(bb,db,b)
    print 'exp: <class \'errval.errval\'> True \ngot: {0} {1}\n---'.format(type(b), isinstance(b,errval))
    
    
    # some arithmetic
    d0, d1, d2 = a+b, b+a, a+2
#    d0+[] # should raise error
    e0, e1, e2 = a-b, a-2, 1-b
#    e0-[] # should raise error
    f0, f1, f2, f3 = a+b+c, a-b+c, a+b-c, b+a-c
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(3,5,d0)
    print 'exp: {0} +- {1} \ngot: {2}\n---'.format(3,5,d1)
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(3,3,d2)
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(-1,5,e0)
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(-1,3,e1)
    print 'exp: {0} +- {1} \ngot: {2}\n---'.format(-1,4,e2)
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(0,np.sqrt(50),f0)
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(-4,np.sqrt(50),f1)
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(6,np.sqrt(50),f2)
    print 'exp: {0} +- {1} \ngot: {2}\n---'.format(6,np.sqrt(50),f3)
    
    g0, g1, g2, g3, g4 = a*b, b*a, a*2, 2*b, a*b*c
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(2,np.sqrt(52),g0)
    print 'exp: {0} +- {1} \ngot: {2}\n---'.format(2,np.sqrt(52),g1)
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(2,6,g2)
    print 'exp: {0} +- {1} \ngot: {2}\n---'.format(4,8,g3)
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(-6,np.sqrt(568),g4)
    
    h0, h1, h2 = a/b, b/2.0, 1.0/c
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(0.5,np.sqrt(3.25),h0)
    print 'exp: {0} +- {1} \ngot: {2}\n---'.format(1,2,h1)
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(1.0/-3,5.0/9,h2)
    
    k0, k1, k2 = a**2, 2**a, b**a
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(1,6,k0)
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(2,np.log(2)*2*3,k1)
    print 'exp: {0} +- {1} \ngot: {2}\n---'.format(2,np.sqrt(16+(np.log(2)*2*3)**2),k2)

    m0 = errval(b,printout='latex!')
    print 'exp: {0} != {1}\ngot: {2}\n---'.format(id(m0),id(b),id(m0)!=id(b))
    print 'exp: {0} \pm {1}\ngot: {2}\n---'.format(b.val(),b.err(),m0)

    n0 = np.sqrt(m0)
    print 'exp: {0} \pm {1} \ngot: {2}\n---'.format(np.sqrt(2),4/(2*np.sqrt(2)),n0)
    
    abc = [a,b,c]
    abcv, abce, abct = values(abc), errors(abc), tuples(abc)
    print 'exp: {0}\ngot: {1}\n---'.format(f0,np.sum(abc))
    print 'exp: {0}\ngot: {1}\n---'.format(zip(abcv,abce),abct)

    abc_ = errvallist([a,b,c])
    print 'exp: <class \'errvallist.errvallist\'> True \ngot: {0} {1}\n---'.format(type(abc_), isinstance(abc_,errvallist))
    print 'Remember: {0}'.format(abc_)
    print 'exp: {0}\ngot: {1}\n---'.format(values(abc),abc_.v())
    print 'exp: {0}\ngot: {1}\n---'.format(errors(abc),abc_.errs())
    print 'exp: {0}\ngot: {1}\n---'.format(f0,np.sum(abc_))
    print 'exp: {0},{1}\ngot: {2},{3}\n---'.format(c,2,min(abc_)[0],min(abc_)[1])

    q0, q1 = errval(100,10), errval(1,1)
    r0, r1 = errval(3.11,0.02), errval(3.13,0.01)
    print 'exp: {0}\ngot: {1}\n---'.format(errval(2,1),wmean([q0,q1]))
    print 'exp: {0}\ngot: {1}\n---'.format(errval(3.126,0.009),wmean([r0,r1])) # [R. Barlow, Statistics, John Wiley & Sons Ltd. (1989)]
    print 'exp: {0}\ngot: {1}\n---'.format(errval(3.126,0.009),wmean(errvallist([r0,r1])))
    print 'exp: {0}\ngot: {1}\n---'.format(errval(50.5,0.5*np.sqrt(101)),np.mean(errvallist([q0,q1])))

    print 'Interpolate:'
    s0,t0 = 1,2
    try: print interp(1.5,s0,t0)
    except TypeError: print 'Non tuple input caught. (Good!)'
    s1,t1 = (1,2),(2,2)
    print 'exp: {0}\ngot: {1}\n---'.format(2,interp(1.5,s1,t1))
    s2,t2 = (1,errval(2,1)),(2,errval(1,0))
    print 'exp: {0}\ngot: {1}\n---'.format(errval(1.5,0.5),interp(1.5,s2,t2))
    s3,t3 = (1,errval(3,1)),(3,(errval(1,3)))
    t3_ = interp(2,s3,t3)
    print 'exp: {0}\ngot: {1}\n---'.format(errval(2,2),t3_)
    s4,t4 = [1,3], errvallist([errval(3,1),errval(1,3)])
    t4_ = interplist(2,s4,t4)
    print 'exp: {0}\ngot: {1}\n---'.format(errval(2,2),t4_)
    
    print 'exp: {0}\ngot: {1}\n---'.format(errval(0.5,0.5),
                                            stderrval([0,1]))
    u = [[1,2,3],[2,3,4]]
    u0 = stderrvallist(u)
    v = errvallist([1.5,2.5,3.5],[0.5,0.5,0.5])
    print 'exp: {0}\ngot: {1}\n---'.format(v,u0)
    


if __name__ == '__main__': main()
