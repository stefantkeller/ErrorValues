#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np
import errorvalues as ev

import pytest

def test_textconversion():
    inpt = 'errval(1,2)*avariable+errval(2,3)' # 'errval()' is output with printout option 'cp': '{}'.format(errval(1,2,'cp'))='errval(1,2)'
    convt = ev.str2errvallist(inpt)
    assert len(convt)==2 # 2 values in string
    assert convt[1].e()==3

    inpt = 'errval(1,2,errvalmode)*avariable+errval(2,3)' # errval(1,2,'cpp'); but only for copy-paste in executed file, where variable errvalmode is specified
    with pytest.raises(ValueError):
        convt = ev.str2errvallist(inpt) # how should I convert errvalmode?!

    inpt = 'errval(1,2)+errvalconst' # attempt of deception doesn't work
    convt = ev.str2errvallist(inpt)
    assert len(convt)==1
    assert convt[0].e()==2

def test_slice():
    lst = [1,2,3]
    elst = ev.errvallist(lst)
    assert '{}'.format(elst[0:2]) == '{}'.format(ev.errvallist(lst[0:2])) # slicing of evlist shows same behavior as in regular list

def test_round():
    ve0 = ev.errvallist([(1.234,0.567),(8.901,2.345)])
    manround = ev.errvallist([(1.23,0.57),(8.9,2.35)])
    assert '{}'.format(ve0.round(2)) == '{}'.format(manround)

