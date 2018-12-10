""" pytest test configures """
from __future__ import print_function

import pytest
import numpy as np

import sisl


pytestmark = [pytest.mark.io, pytest.mark.gulp]
_dir = 'sisl/io/gulp'


def test_zz_dynamical_matrix(sisl_files):
    si = sisl.get_sile(sisl_files(_dir, 'zz.gout'))
    print(si)
    D1 = si.read_dynamical_matrix(order=['got'])
    D2 = si.read_dynamical_matrix(order=['FC'])

    assert D1._csr.spsame(D2._csr)
    D1.finalize()
    D2.finalize()
    assert np.allclose(D1._csr._D, D2._csr._D, atol=1e-5)


def test_zz_sc_geom(sisl_files):
    si = sisl.get_sile(sisl_files(_dir, 'zz.gout'))
    cell = si.read_cell()
    geom = si.read_geometry()
    assert cell == geom.sc
