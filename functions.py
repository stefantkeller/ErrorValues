#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from general_functions import find_index, find_index_iter


'''
functions for dealing with lists containing errvals
not necessarily errvallists
'''


def values(errvallist):
    return np.array([ev.val() for ev in errvallist])
def errors(errvallist):
    return np.array([ev.err() for ev in errvallist])
def tuples(errvallist):
    return zip(values(errvallist),errors(errvallist))

def find_fooval(errvallist,foo,index=False):
    '''
    Find value in list closes to foo(list)
    e.g. foo=max returns the maximum value in the list
    caution: this might not terminate
    (unclear why, open question over at general_functions)
    if not just 'closet' but exact value looked for,
    pick find_fooval_iter
    '''
    v = values(errvallist)
    i = find_index(v,foo(v))
    if index: return errvallist[i], i
    else: return errvallist[i]
def find_fooval_iter(errvallist,foo,index=False):
    '''
    Find value in list corresponding exactly to foo(list)
    e.g. foo=max returns the maximum value in the list
    '''
    v = values(errvallist)
    i = find_index_iter(v,foo(v))
    if index: return errvallist[i], i
    else: return errvallist[i]

def max_(errvallist,index=True):
    # there is only one value,
    # and that one is exact, so go with _iter:
    return find_fooval_iter(errvallist,max,index)
def min_(errvallist,index=True):
    return find_fooval_iter(errvallist,min,index)

def wmean(errvallist):
    '''
    weighted mean

    sigma_<x>^2 = sum(1/sigma_i^2)
    <x> = sum(x_i/sigma_i^2)/sigma_<x>^2
    '''
    printmode = errvallist[0].printout()
    vals = values(errvallist)
    print vals
    errs = errors(errvallist)
    print errs
    N = len(errvallist)
    sig_x = np.sum([1.0/si**2 for si in errs])
    sum_x = np.sum([vals[i]*1.0/errs[i]**2 for i in range(N)])
    return errval(sum_x*1.0/sig_x,1.0/np.sqrt(sig_x),printmode)
    
def interp(v,evxy0,evxy1):
    '''
    linear interpolation between two points
    evxy0 (evxy1) is expected to be a tuple
    representing the x and y value of the
    point to the left (right) of value v
    otherwise it's an extrapolation - proceed with caution!

    Basic idea (for values between v \in [0,1]):
        y = y0 + v*(y1-y0)
    But v is not bound to [0,1], so we have to renormalize:
        v' = (v-x0)/(x1-x0).
    This makes it implicitly clear that we expect x1>x0,
    so, order your input properly!
    We end up:
        y = y0 + (v-x0)/(x1-x0)*(y1-y0).
    '''
    if not isinstance(evxy0,tuple) or not isinstance(evxy1,tuple):
        raise TypeError,\
             'Boundary required as tuple, {0} and {1} given'.format(
                type(evxy0),type(evxy1))
    # if input can be handled with pre-existing functions:
    if not isinstance(evxy0[0],errval) and \
        not isinstance(evxy0[1],errval) and \
        not isinstance(evxy1[0],errval) and \
        not isinstance(evxy1[1],errval):
        return np.interp(v,evxy0,evxy1)
    # ok, at least one of the inputs is errval; worth the time:
    # make sure every entry is indeed errval
    # (because lazy, the x-values don't need to have an error,
    # in fact, if they do this error will be lost)
    x0, y0 = errval(evxy0[0]), errval(evxy0[1])
    x1, y1 = errval(evxy1[0]), errval(evxy1[1])

    scaling = float(v-x0.v())/(x1.v()-x0.v())
    y = y0.v() + scaling*(y1.v()-y0.v())
    ye = y0.e() + scaling*abs(y1.e()-y0.e())
    #scalingy = (y-y0.v())/(y1.v()-y0.v())
    #xe = scalingy*abs(x1.e()-x0.e())
    return errval(y,ye)

def interplist(v,evx,evy):
    '''
    evx must be an ordered (errval,)list or a numpy.ndarray
    evy must be a errvallist
    '''
    if not isinstance(evx,(list,tuple,errvallist,np.ndarray)):
        raise TypeError, 'evx is of unexpected type: {0}'.format(
                type(evx))
    if not isinstance(evy,errvallist):
        raise TypeError, 'This function is for errvallists, try np.interp'
    if isinstance(evx,errvallist):
        evx = evx.v() # errval has only one-dimensional error
    i0 = np.sum([e<=v for e in evx])
    if i0==0: raise ValueError,\
                'Value below interpolation values: {0}<{1}'.format(
                    i0,evx[0])
    xy0 = (evx[i0-1],evy[i0-1])
    xy1 = (evx[i0],evy[i0])
    return interp(v,xy0,xy1)
# ---------------------------------------------------------------------------------------
    

