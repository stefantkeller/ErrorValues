#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np
import errorvalues as ev

import pytest

def test_values_assignments():
    v, e = 1, 3
    ve = ev.errval(v, e)
    assert ve.v() == v
    assert ve.e() == e
    with pytest.raises(ValueError):
        vne = ev.errval(v,-e)
    assert '{}'.format(ev.errval(1)) == '{}'.format(ev.errval(1,0))
    assert isinstance(ve,ev.errval)

def test_values_assignment_tuples():
    tpl2 = (1,3)
    tpl3 = (1,3,'+-')
    assert r'{}'.format(ev.errval(1.0,3.0)) == r'{}'.format(ev.errval(tpl2))
    assert r'{}'.format(ev.errval(1.0,3.0,'+-')) == r'{}'.format(ev.errval(tpl3))

def test_format():
    v, e = 1, 3
    ve0 = ev.errval(v, e)
    assert r'{}'.format(ve0) == r'{} \pm {}'.format(v,e)
    ve1 = ev.errval(v, e, '+-')
    assert r'{}'.format(ve1) == r'{} +- {}'.format(v,e)
    ve2 = ev.errval(v, e, 'cp')
    assert r'{}'.format(ve2) == r'errval({},{})'.format(v,e)
    ve3 = ev.errval(v, e, 'cpp')
    assert r'{}'.format(ve3) == r'errval({},{},errvalmode)'.format(v,e)
    ve4 = ev.errval(ve3,printout='latex!')
    assert r'{}'.format(ve4) == r'{}'.format(ve0)
    assert id(ve4) != id(ve0)

def test_arithmetic():
    ve0 = ev.errval(1,3)
    ve1 = ev.errval(2,4,'+-')

    assert r'{}'.format(ve0+ve1) == r'3 \pm 5.0' # basic addition
    assert r'{}'.format(ve1+ve0) == r'3 +- 5.0' # printout according left input
    assert r'{}'.format(ve0+2) == r'3 \pm 3' # regular int
    assert r'{}'.format(ve0+3.0) == r'4.0 \pm 3' # regular float

    assert r'{}'.format(ve0-ve1) == r'-1 \pm 5.0'
    assert r'{}'.format(ve0-2) == r'-1 \pm 3'
    
    assert r'{}'.format(ve0*ve1) == r'{}'.format(ev.errval(2,np.sqrt(52)))

    assert r'{}'.format(ve1/2.0) == r'1.0 +- 2.0'
    assert r'{}'.format(ve1/2) == r'1.0 +- 2.0'
    
    assert r'{}'.format(ve0**2) == r'1 \pm 6'
