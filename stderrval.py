#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt




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



