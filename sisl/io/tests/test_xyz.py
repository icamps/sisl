# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import pytest
import os.path as osp
import numpy as np
from sisl.io.xyz import *


pytestmark = [pytest.mark.io, pytest.mark.generic]
_dir = osp.join('sisl', 'io')


def test_xyz1(sisl_tmp, sisl_system):
    f = sisl_tmp('gr.xyz', _dir)
    sisl_system.g.write(xyzSile(f, 'w'))
    g = xyzSile(f).read_geometry()

    # Assert they are the same
    assert np.allclose(g.cell, sisl_system.g.cell)
    assert np.allclose(g.xyz, sisl_system.g.xyz)
    assert sisl_system.g.atoms.equal(g.atoms, R=False)
    g = xyzSile(f).read_geometry(sc=g.sc)
    assert np.allclose(g.cell, sisl_system.g.cell)


def test_xyz_sisl(sisl_tmp):
    f = sisl_tmp('sisl.xyz', _dir)
    open(f, 'w').write("""3
sisl-version=1 nsc=1 1 3 cell=10 0 0 0 12 0 0 0 13
C   0.00000000  0.00000000  0.00000000
C   1.000000  0.00000000  0.00000000
C   2.00000  0.00000000  0.00000000
""")
    g = xyzSile(f).read_geometry()

    # Assert they are the same
    assert np.allclose(g.cell, [[10, 0, 0], [0, 12, 0], [0, 0, 13]])
    assert np.allclose(g.xyz[:, 0], [0, 1, 2])
    assert np.allclose(g.xyz[:, 1], 0.)
    assert np.allclose(g.xyz[:, 2], 0.)
    assert np.allclose(g.nsc, [1, 1, 3])

    g = xyzSile(f).read_geometry(sc=[10, 11, 13])
    assert np.allclose(g.cell, [[10, 0, 0], [0, 11, 0], [0, 0, 13]])


def test_xyz_ase(sisl_tmp):
    f = sisl_tmp('ase.xyz', _dir)
    open(f, 'w').write("""3
Lattice="10 0 0 0 12 0 0 0 13" Properties=species:S:1:pos:R:3 pbc="F F T"
C   0.00000000  0.00000000  0.00000000
C   1.000000  0.00000000  0.00000000
C   2.00000  0.00000000  0.00000000
""")
    g = xyzSile(f).read_geometry()

    # Assert they are the same
    assert np.allclose(g.cell, [[10, 0, 0], [0, 12, 0], [0, 0, 13]])
    assert np.allclose(g.xyz[:, 0], [0, 1, 2])
    assert np.allclose(g.xyz[:, 1], 0.)
    assert np.allclose(g.xyz[:, 2], 0.)
    assert np.allclose(g.nsc, [1, 1, 3])


def test_xyz_arbitrary(sisl_tmp):
    f = sisl_tmp('ase.xyz', _dir)
    open(f, 'w').write("""3

C   0.00000000  0.00000000  0.00000000
C   1.000000  0.00000000  0.00000000
C   2.00000  0.00000000  0.00000000
""")
    g = xyzSile(f).read_geometry()

    # Assert they are the same
    assert np.allclose(g.xyz[:, 0], [0, 1, 2])
    assert np.allclose(g.xyz[:, 1], 0.)
    assert np.allclose(g.xyz[:, 2], 0.)
    assert np.allclose(g.nsc, [1, 1, 1])
