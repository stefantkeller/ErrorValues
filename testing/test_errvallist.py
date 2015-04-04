#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np
import errorvalues as ev

import pytest

def test_convenience():
    a, b, c = ev.errval(1,3), ev.errval(2,4), ev.errval(3,5)
    abc = [a,b,c]
    abcv = [1,2,3]
    abce = [3,4,5]
    valus = ev.values(abc)
    errrs = ev.errors(abc)
    tupls = ev.tuples(abc)
    for j in xrange(len(abc)):
        assert abcv[j] == valus[j]
        assert abce[j] == errrs[j]
        assert tupls[j] == (valus[j],errrs[j])

def test_len():
    a, b, c = ev.errval(1,3), ev.errval(2,4), ev.errval(3,5)
    abc = ev.errvallist([a,b,c])
    assert len(abc) == 3

def test_list_assignment():
    a, b, c = ev.errval(1,3), ev.errval(2,4), ev.errval(3,5)
    abc = ev.errvallist([a,b,c])
    assert isinstance(abc,ev.errvallist)
    abcv = [1,2,3]
    abce = [3,4,5]
    valus = abc.v()
    errrs = abc.e()
    for j in xrange(len(abc)):
        assert abcv[j] == valus[j]
        assert abce[j] == errrs[j]

def test_list_assignment_fail():
    with pytest.raises(ValueError):
        ev.errvallist('text input')

def test_list_assignment_tuples():
    proper_errval = ev.errval(1,3)
    simple_tuple = (1,3)
    L1 = ev.errvallist([proper_errval])
    L2 = ev.errvallist([simple_tuple])
    assert L1.v()[0]==L2.v()[0]
    assert L1.e()[0]==L2.e()[0]
    assert L1[0].v()==L2[0].v()
    assert L1[0].e()==L2[0].e()

def test_list_summation():
    a, b, c = ev.errval(1,3), ev.errval(2,4), ev.errval(3,5)
    abc = ev.errvallist([a,b,c])
    abc_sum = np.sum(abc)
    abc_sum1 = a+b+c
    assert abc_sum.v() == abc_sum1.v()
    assert abc_sum.e() == abc_sum1.e()
    
def test_wmean():
    a, b = ev.errval(100,10), ev.errval(1,1)
    assert r'2.0 \pm 1.0' == '{}'.format(ev.wmean(ev.errvallist([a,b])).round(1))
    assert r'2.0 \pm 1.0' == '{}'.format(ev.wmean([a,b]).round(1))

def test_interpolate_fail():
    with pytest.raises(TypeError):
        ev.interp(1.5,1,2) # input not appropriate for interpolation

def test_interpolate():
    lft, rgt = (1,2), (2,2)
    assert r'2.0' == r'{}'.format(ev.interp(1.5,lft,rgt))

    lft_yerr, rgt_yerr = (1,ev.errval(3,1)),(3,ev.errval(1,3))
    interp_yerr = ev.interp(2,lft_yerr,rgt_yerr)
    assert r'2.0 \pm 2.0' == r'{}'.format(interp_yerr)

def test_interpolate_list():
    evx, evy = [1,3], ev.errvallist([ev.errval(3,1),ev.errval(1,3)])
    ev_interp = ev.interplist(2,evx,evy)
    assert r'2.0 \pm 2.0' == r'{}'.format(ev_interp)

def test_stderrvallist():
    a = [[1,2,3],[2,3,4]]
    a0 = ev.stderrvallist(a)
    b = ev.errvallist([1.5,2.5,3.5],[0.5,0.5,0.5])
    for j in xrange(len(b)):
        assert a0[j].v() == b[j].v()
        assert a0[j].e() == b[j].e()
