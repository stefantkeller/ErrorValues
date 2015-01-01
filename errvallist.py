#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Work with whole lists of errval's:
 [v0+-e0, v1+-e1, ...]
'''

import numpy as np

from errval import *


class errvallist(list):
    def __init__(self,vals,errs=0,printout='latex'):
        if isinstance(vals,errvallist):
            self.__errl = vals
        elif isinstance(vals,(list,np.ndarray)) or isinstance(errs,(list,np.ndarray)):
            if isinstance(vals,(list,np.ndarray)) and isinstance(errs,(list,np.ndarray)):
                if len(vals)==len(errs):
                    self.__errl = [errval(vals[j],errs[j],printout) for j in xrange(len(vals))]
            elif isinstance(vals,(list,np.ndarray)) and isinstance(errs,(int,float,long)):
                # note: this also covers the case vals is a list of errval entries,
                # in this case the errs are ignored and the result is a conversion of list to errvallist
                self.__errl = [errval(v,errs,printout) for v in vals]
            elif isinstance(vals,(int,float,long)) and isinstance(errs,(list,np.ndarray)):
                self.__errl = [errval(vals,e,printout) for e in errs]
        else:
            raise ValueError, 'Cannot assign input data: {0}'.format(type(vals))

    def __getitem__(self,key):
        return self.__errl[key]
    def __setitem__(self,key,value):
        self.__errl[key]=value

    def __getslice__(self,i,j):
        # https://docs.python.org/2/reference/datamodel.html#object.__getslice__
        # Deprecated since version 2.0
        # but since I derive from list I have to ignore this deprecation...
        return errvallist(self.__errl[i:j])

    def __str__(self):
        outp = '['
        for evl in self.__errl:
            outp += evl.__str__()+','
        outp = outp[:-1]+']'
        return outp
    
    def __iter__(self):
        # to make the errvallist iterable
        # i.e. to make the 'in' possible in 'for err in errvallist:'
        for err in self.__errl:
            yield err

    def __len__(self):
        return len(self.__errl)

    def __add__(self,other):
        if isinstance(other,(errvallist,list)) and len(self)==len(other):
             errvall = [self[j]+other[j] for j in xrange(len(self))]
        elif isinstance(other,(int,float,long,errval)):
            errvall = [s+other for s in self]
        else:
            raise TypeError, 'unsupported operand type(s) for +: errval with {0}'.format(type(other))
        return errvallist(errvall)
    def __radd__(self,other):
            return self.__add__(other)

    def __sub__(self,other):
        if isinstance(other,(errvallist,list)) and len(self)==len(other):
            errvall = [self[j]-other[j] for j in xrange(len(self))]
        elif isinstance(other,(int,float,long,errval)):
            errvall = [s-other for s in self]
        else:
            raise TypeError, 'unsupported operand type(s) for -: errval with {0}'.format(type(other))
        return errvallist(errvall)
    def __rsub__(self,other):
        return -1*self.__sub__(other)

    def __mul__(self,other):
        if isinstance(other,(errvallist,list)) and len(self)==len(other):
            errvall = [self[j]*other[j] for j in xrange(len(self))]
        elif isinstance(other,(int,float,long,errval)):
            errvall = [s*other for s in self]
        else:
            raise TypeError, 'unsupported operand type(s) for *: errval with {0}'.format(type(other))
        return errvallist(errvall)
    def __rmul__(self,other):
        return self.__mul__(other)

    def __div__(self,other):
        if isinstance(other,(errvallist,list)) and len(self)==len(other):
            errvall = [self[j]/other[j] for j in xrange(len(self))]
        elif isinstance(other,(int,float,long,errval)):
            errvall = [s/other for s in self]
        else:
            raise TypeError, 'unsupported operand type(s) for /: errval with {0}'.format(type(other))
        return errvallist(errvall)
    def __rdiv__(self,other):
        return 1.0/self.__div__(other)

    def append(self,value):
        self.__errl.append(value)

    '''
    Depending on the circumstances the code incorporating this class
    may want to use different names for the following functions:
    '''
    def v(self): return np.array([ev.val() for ev in self])
    def val(self): return self.v()
    def vals(self): return self.v()
    def values(self): return self.v()

    def e(self): return np.array([ev.err() for ev in self])
    def err(self): return self.e()
    def errs(self): return self.e()
    def errors(self): return self.e()


