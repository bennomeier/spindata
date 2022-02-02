"""spindata

spindata provides the functions gamma, spin and qaudrupole.

Each argument takes a string as an argument which specifies the isotope (e.g. "1H" or "2H") or the electron ("E").

The return values of all functions are floats.

The polarization module provides a routine to calculate the thermal polarization for given spin, magnetic field and temperature.

Written by Benno Meier with contributions from Tobias Lehmann."""

from .gamma import gamma
from .spin import spin
from .quadrupolemoment import quadrupole
from .polarization import polarization, magnetization

__all__ = [gamma, spin, quadrupole, polarization, magnetization]
