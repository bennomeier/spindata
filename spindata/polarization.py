"""Calculate the thermal polarization of a given nucleus for a given field and temperature."""

from scipy.constants import k, hbar, N_A
from spindata.gamma import gamma
from spindata.spin import spin
import numpy as np

#  P = N \left ( \frac{2}{1 + \exp ( - \Delta E / k_B T)} - 1 \right ) = Tanh( \Delta e / 2 k_B T)

def polarization(nucleus, B, T):
    """This function returns the thermal polarization at a given temperature and field.
    If nucleus equals "E", then the electron gamma is chosen.
    Arguments:
    - `nucleus`: String describing the nucleus, e.g., "1H", "13C" or "E" for electrons
    - `B`: Magnetic Field in Tesla
    - `T`: Temperature in Kelvin
    """
    g = gamma(nucleus)
    DE = hbar*g*B
    
    polarization = np.tanh(DE/(2*k*T))
    return polarization

def magnetization(nucleus, B, T, concentration, unit = "mol"):
    """This function returns the thermal magnetiazation at a given temperature and field.

    The magnetisation corresponds to dipole moment per volume. The dipole moment of a single spin is mz = gamma hbar Iz.

    Therefore we only need to calculate the trace of rho m_z and multiply with the number density.

    If nucleus equals "E", then the electron gamma is chosen.
    Arguments are as for the polarization, concentration is in mol by default, but can be specified as "numberDensity"

    The function returns the magnetization in A/m.
    """

    # let us assume that the Zeeman interaction dominates. Then

    p = polarization(nucleus, B, T)

    I = spin(nucleus)
    g = gamma(nucleus)

    #calculate the trace
    Z =  np.sum([np.exp(- hbar*g*B*mz/(k*T)) for mz in list(np.arange(-I, I+1))])

    #for mZ we have to do the same trace operation bult multiplz with Iz gamm hbar

    mZ = g*hbar/Z*np.sum([np.exp(hbar*g*B*mz/(k*T))*mz for mz in list(np.arange(-I, I+1))])

    if unit == "numberDensity":
        n = concentration
    elif unit == "mol":
        n = concentration*N_A*1e3

    #this is the high temperature approximation, or Curie Law.
    MzHighTemp = n*g**2*hbar**2*B*I*(I+1) / (3 * k * T)

    Mz = n*mZ

    #print("highTemp: ", MzHighTemp)
    #print("QM: ", Mz)
    return Mz

if __name__ == "__main__":
    print("E polarization at 3.35 Tesla, 1 K: {}".format(polarization("E", 3.35, 1)))
    print("13C polarization at 3.35 Tesla, 1.5K: {}".format(polarization("13C", 3.35, 1)))
    print("13C polarization at 9 Tesla, 300K: {}".format(polarization("13C", 9, 300)))
    print("Ratio between E and 13C those: {}".format(polarization("E", 3.35, 1.5)/polarization("13C", 9, 300)))
    print("The bulk magnetic moment of pure HDO (55 molar) due to protons at 9.4 Tesla and 290 K is: {:.3f} A/m".format(magnetization("1H", 9.4, 290,  55)))
