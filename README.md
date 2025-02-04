# sisl #

[![Install sisl using PyPI](https://badge.fury.io/py/sisl.svg)](https://badge.fury.io/py/sisl)
[![Install sisl using conda](https://anaconda.org/conda-forge/sisl/badges/version.svg)](https://anaconda.org/conda-forge/sisl)
[![DOI for citation](https://zenodo.org/badge/doi/10.5281/zenodo.597181.svg)](http://dx.doi.org/10.5281/zenodo.597181)
[![Join discussion on Discord](https://img.shields.io/discord/742636379871379577.svg?label=&logo=discord&logoColor=ffffff&color=green&labelColor=red)](https://discord.gg/5XnFXFdkv2)
<!--- [![Documentation on RTD](https://readthedocs.org/projects/docs/badge/?version=latest)](http://sisl.readthedocs.io/en/latest/) -->
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://www.mozilla.org/en-US/MPL/2.0/)
[![Build Status](https://travis-ci.com/zerothi/sisl.svg?branch=master)](https://travis-ci.com/zerothi/sisl)
[![Checkout sisl code coverage](https://codecov.io/gh/zerothi/sisl/branch/master/graph/badge.svg)](https://codecov.io/gh/zerothi/sisl)

## Why sisl ##

The Python library sisl was born out of a need to handle(create and read), manipulate and analyse output from DFT programs.
It was initially developed by Nick Papior (co-developer of [Siesta][siesta]) as a side-project to TranSiesta
and TBtrans to efficiently analyse TBtrans output for N-electrode calculations.  
Since then it has expanded to accommodate a rich set of DFT code input/outputs such as (but not limited to)
VASP, OpenMX, BigDFT, Wannier90.

A great deal of codes are implementing, roughly, the same thing.
However, every code implements their own analysis and post-processing utilities which typically
turns out to be equivalent utilities only having the interface differently.

sisl tries to solve some of the analysis issues by creating a unified scripting approach
in Python which does analysis using the same interface, regardless of code being used.
For instance one may read the Kohn-Sham eigenvalue spectrum from various codes and return them
in a consistent manner so the post-processing is the same, regardless of code being used.

sisl is also part of the training material for a series of workshops hosted [here][workshop].

In some regards it has overlap with [ASE][ase] and sisl also interfaces with ASE.

### Example use ###

Here we show 2 examples of using sisl together with [Siesta][siesta].

To read in a Hamiltonian from a Siesta calculation and calculate the DOS for a given Monkhorst-Pack grid
one would do:

    import numpy as np
    import sisl
    H = sisl.get_sile('RUN.fdf').read_hamiltonian()
    mp = sisl.MonkhorstPack(H, [13, 13, 13])
    E = np.linspace(-4, 4, 500)
    DOS = mp.apply.average.DOS(E)
    from matplotlib import pyplot as plt
    plt.plot(E, DOS)

Which calculates the DOS for a 13x13x13 Monkhorst-Pack grid.

Another common analysis is real-space charge analysis, the following command line subtracts two real-space
charge grids and writes them to a CUBE file:

    sgrid reference/Rho.grid.nc --diff Rho.grid.nc --geometry RUN.fdf --out diff.cube

which may be analysed using VMD, XCrySDen or other tools.


## Installation ##

Installing sisl using PyPi or Conda is the easiest:

    python3 -m pip install sisl
    python3 -m pip install sisl[analysis] # also installs tqdm and xarray
    # or
    conda install -c conda-forge sisl

If performing a manual installation, these packages are required:

   - A C- and fortran-compiler
   - __Cython__ (0.28 or later)
   - __numpy__ (1.13 or later)
   - __scipy__ (0.18 or later)
   - __netCDF4__
   - __setuptools__
   - __pyparsing__ (1.5.7 or later)
   - __pytest__, optional dependency for running the tests
   - __matplotlib__, encouraged optional dependency
   - __tqdm__, encouraged optional dependency
   - __xarray__, optional dependency
   - __plotly__, optional dependency

Subsequently manual installation may be done using this command:

    python3 setup.py install --prefix=<prefix>

If trying to install without root access, you may be required to use this command:

    python3 setup.py install --user --prefix=<prefix>


Once installed, the installation can be tested by executing the following:

    pytest --pyargs sisl

## Everyday use of sisl ##

There are different places for getting information on using sisl, here is a short list
of places to search/ask for answers:

- [Documentation][sisl-api], recommended reference page
- [Workshop][workshop] examples showing different uses
- Ask questions on the Github [issue page][issue]
- Ask questions on the [Gitter page][sisl-gitter]

If sisl was used to produce scientific contributions, please use this [DOI][doi] for citation.
We recommend to specify the version of sisl in combination of this citation:

    @misc{zerothi_sisl,
      author = {Papior, Nick},
      title  = {sisl: v<fill-version>},
      year   = {2021},
      doi    = {10.5281/zenodo.597181},
      url    = {https://doi.org/10.5281/zenodo.597181}
    }

To get the BibTeX entry easily you may issue the following command:

    sdata --cite

which fills in the version number.

## Help sisl help you! ##

If you have

- ideas of missing features
- ideas for improving documentation
- found a bug
- found a documentation error
- created a tutorial

Then please share them [here][issue]!

All of the above may be done via a [pull-request][pr] or by opening
an [issue].

Remember:

> No contribution is too small!


<!---
Links to external and internal sites.
-->
[sisl@git]: https://github.com/zerothi/sisl
[sisl-api]: https://zerothi.github.io/sisl
[sisl-gitter]: https://gitter.im/sisl-tool/Lobby
[issue]: https://github.com/zerothi/sisl/issues
[pr]: https://github.com/zerothi/sisl/pulls
[siesta]: https://gitlab.com/siesta-project/siesta
[tbtrans]: https://gitlab.com/siesta-project/siesta
[workshop]: https://github.com/zerothi/ts-tbt-sisl-tutorial
[doi]: http://dx.doi.org/10.5281/zenodo.597181
[mpl]: https://www.mozilla.org/en-US/MPL/2.0/
[ase]: https://wiki.fysik.dtu.dk/ase/

<!---
Local variables for emacs to turn on flyspell-mode
% Local Variables:
%   mode: flyspell
%   tab-width: 4
%   indent-tabs-mode: nil
% End:
-->

