#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt


class errval(object):
    def __init__(self,val,err=0,printout='latex'):
        '''
        val = the value (number or errval (see below))
        err = the corresponding error
        printout = what 'print' should look like

        if you initiate with val=errval a copy of that input errval is provided
        if you then want to change the printout value for that copy you have
        two choices:
            (1) a posteriori with .printout('mynewopt')
            (2) by specifying the new option with a !bang:
                cp = errval(orig,printout='mynewopt!')
        '''
        if isinstance(val,errval): # return copy
            self.__val = val.val()
            self.__assign_err(val.err())
            self.__printout = val.printout()
            if printout.endswith('!'): self.__printout = printout
        elif ( isinstance(val,tuple) and len(val)==2
               and isinstance(val[0],(int,float,long)) and isinstance(val[1],(int,float,long)) ):
            self.__val = val[0]
            self.__assign_err(val[1])
            self.__printout = printout
        elif ( isinstance(val,tuple) and len(val)==3
               and isinstance(val[0],(int,float,long)) and isinstance(val[1],(int,float,long))
               and isinstance(val[2],str) ):
            self.__val = val[0]
            self.__assign_err(val[1])
            self.__printout = val[2]
        elif isinstance(val,(int,float,long)):
            self.__val = val
            self.__assign_err(err)
            self.__printout = printout
        else:
            raise ValueError, 'Cannot assign input data'

    
    def val(self):
        return self.__val
    def err(self):
        return self.__err
    def v(self):
        return self.__val
    def e(self):
        return self.__err
    def printout(self,change=''):
        if change!='':
            self.__printout = change
        return self.__printout


    def __str__(self):
        '''
        called by print
        output depends on initialization
        when two errvals are put together the result has the value of the left one
        '''
        if self.__printout == '+-':
            return "{0} +- {1}".format(self.__val,self.__err)
        if self.__printout == 'cp': # make it easier to copy paste...
            return "errval({0},{1})".format(self.val(),self.err())
        if self.__printout == 'cpp': # make it easier to copy paste...
            return "errval({0},{1},errvalmode)".format(self.val(),self.err())
        else: # default = latex
            return "{0} \pm {1}".format(self.__val,self.__err)

    def __assign_err(self,err):
        if err<0: raise ValueError, 'Cannot assign negative error'
        else: self.__err = err
    
    def __add__(self,other):
        if isinstance(other,errval):
            nval = self.val() + other.val()
            nerr = np.sqrt( self.err()**2 + other.err()**2 )
        elif isinstance(other,(int,float,long)):
            # a value with zero error attached
            nval = self.val() + other
            nerr = self.err()
        else:
            raise TypeError, 'unsupported operand type(s) for +: errval with {0}'.format(type(other))
        return errval(nval, nerr, self.__printout)
    def __radd__(self,other):
        return self.__add__(other)
    
    def __sub__(self,other):
        if isinstance(other,errval):
            nval = self.val() - other.val()
            nerr = np.sqrt( self.err()**2 + other.err()**2 )
        elif isinstance(other,(int,float,long)):
            # a value with zero error attached
            nval = self.val() - other
            nerr = self.err()
        else:
            raise TypeError, 'unsupported operand type(s) for -: errval with {0}'.format(type(other))
        return errval(nval, nerr, self.__printout)
    def __rsub__(self,other):
        if isinstance(other,(int,float,long)):
            # a value with zero error attached
            nval = other - self.val()
            nerr = self.err()
        else:
            raise TypeError, 'unsupported operand type(s) for -: {0} with errval'.format(type(other))
        return errval(nval, nerr, self.__printout)
        
    def __mul__(self,other):
        if isinstance(other,errval):
            nval = self.val() * other.val()
            nerr = np.sqrt( (other.val()*self.err())**2 + (self.val()*other.err())**2 )
        elif isinstance(other,(int,float,long)):
            # a value with zero error attached
            nval = self.val() * other
            nerr = self.err() * abs(other)
        else:
            raise TypeError, 'unsupported operand type(s) for *: errval with {0}'.format(type(other))
        return errval(nval, nerr, self.__printout)
    def __rmul__(self,other):
        return self.__mul__(other)
    
    def __div__(self,other):
        if isinstance(other,errval):
            nval = self.val() *1.0 / other.val()
            nerr = np.sqrt( (1.0/other.val()*self.err())**2 + (self.val()*1.0/(other.val()**2)*other.err())**2 )
        elif isinstance(other,(int,float,long)):
            # a value with zero error attached
            nval = self.val() *1.0 / other
            nerr = self.err() *1.0/ abs(other)
        else:
            raise TypeError, 'unsupported operand type(s) for /: errval with {0}'.format(type(other))
        return errval(nval, nerr, self.__printout)
    def __rdiv__(self,other):
        if isinstance(other,(int,float,long)):
            # a value with zero error attached
            nval = other *1.0/self.val()
            nerr = abs(other)*1.0/self.val()**2 * self.err()
        else:
            raise TypeError, 'unsupported operand type(s) for /: {0} with errval'.format(type(other))
        return errval(nval, nerr, self.__printout)
    
    def __pow__(self,other):
        if isinstance(other,errval):
            nval = self.val() ** other.val()
            nerr = np.sqrt( ( other.val() * self.val()**(other.val()-1) * self.err() )**2
                            + ( np.log(self.val()) * self.val()**other.val() * other.err() )**2 )
        elif isinstance(other,(int,float,long)):
            # a value with zero error attached
            nval = self.val() ** other
            nerr = abs( other * self.val()**(other-1) * self.err() )
        else:
            raise TypeError, 'unsupported operand type(s) for **: errval with {0}'.format(type(other))
        return errval(nval, nerr, self.__printout)
    def __rpow__(self,other):
        if isinstance(other,(int,float,long)):
            # a value with zero error attached
            nval = other ** self.val()
            nerr = abs( np.log(other) * other**self.val() * self.err() )
        else:
            raise TypeError, 'unsupported operand type(s) for **: errval with {0}'.format(type(other))
        return errval(nval, nerr, self.__printout)
    
    def __abs__(self):
        return errval(abs(self.val()), self.err(), self.printout())
    
    def sqrt(self):
        return self**0.5

    def round(self,n=0):
        # returns new instance
        return errval(np.around(self.val(),n),np.around(self.err(),n),self.printout())

