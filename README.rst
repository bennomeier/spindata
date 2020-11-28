Spindata
--------

Spindata provides the gyromagnetic ratio, the spin and the quadrupole moment of all isotopes carrying spin, and the electron.

Spindata is available on PyPi and can be installed as follows:

>>> pip install spindata

Alternatively, download the repository from github and run

>>> python setup.py install

To access these data call spindata's routines gamma, spin and quadrupole, respectively.

Like so::

>>> import spindata
>>> print(spindata.gamma("1H"))
>>> print(spindata.spin("17O"))
>>> print(spindata.quadrupole("17O"))

To calculate the thermal equilibrium polarization of e.g. electron spins at 6.7 Tesla and 1 Kelvin do

>>> print(spindata.polarization("E", 6.7, 1))

To calculate the thermal equilibrium bulk magnetization (in A/m) of e.g. 15 mM electron spins at 6.7 Tesla and 1 Kelvin do

>>> print(spindata.magnetization("E", 6.7, 1, 15e-3))

This assumes that the Zeeman interaction dominates the Hamiltonian.

