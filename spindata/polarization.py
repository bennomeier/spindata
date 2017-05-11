"""Calculate the thermal polarization of a given nucleus for a given field and temperature."""

from scipy.constants import k, hbar
from spindata.gamma import gamma
import numpy as np

#  P = N \left ( \frac{2}{1 + \exp ( - \Delta E / k_B T)} - 1 \right )

def polarization(nucleus, B, T):
    """This function returns the thermal polarization at a given temperature.
    If nucleus equals "E", then the electron gamma is chosen.
    Arguments:
    - `nucleus`: String describing the nucleus, e.g., "1H", "13C" or "E" for electrons
    - `B`: Magnetic Field in Tesla
    - `T`: Temperature in Kelvin
    """
    g = gamma(nucleus)
    DE = hbar*g*B
    polarization = 2/(1 + np.exp(- DE/(k*T))) -1

    return polarization

if __name__ == "__main__":
    print "E polarization at 3.35 Tesla, 1 K: ", polarization("E", 3.35, 1)
    print "13C polarization at 3.35 Tesla, 1.5K: ", polarization("13C", 3.35, 1)
    print "13C polarization at 9 Tesla, 300K: ", polarization("13C", 9, 300)
    print "1H polarization at 11.7 Tesla, 300K: ", polarization("1H", 11.7, 300)
    print "Ratio between those: ", polarization("E", 3.35, 1.5)/polarization("13C", 9, 300)
