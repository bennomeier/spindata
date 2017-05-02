Spindata
--------

Spindata provides the gyromagnetic ratio, the spin and the quadrupole moment of all isotopes carrying spin, and the electron.

To access these data call spindata's routines gamma, spin and quadrupole, respectively.

Like so::

    >>> import spindata
    >>> print(spindata.gamma("1H"))
    >>> print(spindata.spin("17O"))
    >>> print(spindata.quadrupole("17O"))
