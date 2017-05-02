""" This module contains the quadrupole moment for all quadrupolar nuclei.
Based on  

R. K. Harris et al., NMR nomenclature. Nuclear spin properties and conventions for chemical shifts(IUPAC Recommendations 2001) 
Pure Appl. Chem., Vol. 73, No. 11, pp. 1795-1818, 2001.
https://doi.org/10.1351/pac200173111795

The values are stored in the dictionary quadrupoleListAll.

The function quadrupole(nuc) will return the quadrupole moment of nucleus nuc, which is specified e.g. as "2H"
"""

quadrupoleListAll = {}

# Quadrupolar Isotopes
quadrupoleListAll["2H"] = 0.2860e-28 # Deuterium
quadrupoleListAll["6Li"] = -0.0808e-28 # Lithium
quadrupoleListAll["7Li"] = -4.01e-28 # Lithium
quadrupoleListAll["9Be"] = 5.288e-28 # Beryllium
quadrupoleListAll["10B"] = 8.459e-28 # Boron
quadrupoleListAll["11B"] = 4.059e-28 # Boron
quadrupoleListAll["14N"] = 2.044e-28 # Nitrogen
quadrupoleListAll["17O"] = -2.558e-28 # Oxygen
quadrupoleListAll["21Ne"] = 10.155e-28 # Neon
quadrupoleListAll["23Na"] = 10.4e-28 # Sodium
quadrupoleListAll["25Mg"] = 19.94e-28 # Magnesium
quadrupoleListAll["27Al"] = 14.66e-28 # Aluminum
quadrupoleListAll["33S"] = -6.78e-28 # Sulphur
quadrupoleListAll["35Cl"] = -8.165e-28 # Chlorine
quadrupoleListAll["37Cl"] = -6.435e-28 # Chlorine
quadrupoleListAll["39K"] = 5.85e-28 # Potassium
quadrupoleListAll["40K"] = -7.3e-28 # Potassium
quadrupoleListAll["41K"] = 7.11e-28 # Potassium
quadrupoleListAll["43Ca"] = -4.08e-28 # Calcium
quadrupoleListAll["45Sc"] = -22.0e-28 # Scandium
quadrupoleListAll["47Ti"] = 30.2e-28 # Titanium
quadrupoleListAll["49Ti"] = 24.7e-28 # Titanium
quadrupoleListAll["50V"] = 21.0e-28 # Vanadium
quadrupoleListAll["51V"] = -5.2e-28 # Vanadium
quadrupoleListAll["53Cr"] = -15.0e-28 # Chromium
quadrupoleListAll["55Mn"] = 33.0e-28 # Manganese
quadrupoleListAll["59Co"] = 42.0e-28 # Cobalt
quadrupoleListAll["61Ni"] = 16.2e-28 # Nickel
quadrupoleListAll["63Cu"] = -22.0e-28 # Copper
quadrupoleListAll["65Cu"] = -20.4e-28 # Copper
quadrupoleListAll["67Zn"] = 15.0e-28 # Zinc
quadrupoleListAll["69Ga"] = 17.1e-28 # Gallium
quadrupoleListAll["71Ga"] = 10.7e-28 # Gallium
quadrupoleListAll["73Ge"] = -19.6e-28 # Germanium
quadrupoleListAll["75As"] = 31.4e-28 # Arsenic
quadrupoleListAll["79Br"] = 31.3e-28 # Bromine
quadrupoleListAll["81Br"] = 26.2e-28 # Bromine
quadrupoleListAll["83Kr"] = 25.9e-28 # Krypton
quadrupoleListAll["85Rb"] = 27.6e-28 # Rubidium
quadrupoleListAll["87Rb"] = 13.35e-28 # Rubidium
quadrupoleListAll["87Sr"] = 33.5e-28 # Strontium
quadrupoleListAll["91Zr"] = -17.6e-28 # Zirconium
quadrupoleListAll["93Nb"] = -32.0e-28 # Niobium
quadrupoleListAll["95Mo"] = -2.2e-28 # Molybdenum
quadrupoleListAll["97Mo"] = 25.5e-28 # Molybdenum
quadrupoleListAll["99Tc"] = -12.9e-28 # Technetium
quadrupoleListAll["99Ru"] = 7.9e-28 # %Ruthenium
quadrupoleListAll["101Ru"] = 45.7e-28 # Ruthenium
quadrupoleListAll["105Pd"] = 66.0e-28 # Palladium
quadrupoleListAll["113In"] = 79.9e-28 # Indium
quadrupoleListAll["115In"] = 81.0e-28 # Indium
quadrupoleListAll["121Sb"] = -36.0e-28 # Antimony
quadrupoleListAll["123Sb"] = -49.0e-28 # Antimony
quadrupoleListAll["127I"] = -71.0e-28 # Iodine
quadrupoleListAll["131Xe"] = -11.4e-28 # Xenon
quadrupoleListAll["133Cs"] = -0.343e-28 # Caesium
quadrupoleListAll["135Ba"] = 16.0e-28 # Barium
quadrupoleListAll["137Ba"] = 24.5e-28 # Barium
quadrupoleListAll["138La"] = 45.0e-28 # Lanthanum
quadrupoleListAll["139La"] = 20.0e-28 # Lanthanum
quadrupoleListAll["177Hf"] = 336.5e-28 # Hafnium
quadrupoleListAll["179Hf"] = 379.3e-28 # Hafnium
quadrupoleListAll["181Ta"] = 317.0e-28 # Tantalum
quadrupoleListAll["185Re"] = 218.0e-28 # Rhenium
quadrupoleListAll["187Re"] = 207.0e-28 # Rhenium
quadrupoleListAll["189Os"] = 85.6e-28 # Osmium
quadrupoleListAll["191Ir"] = 81.6e-28 # Iridium
quadrupoleListAll["193Ir"] = 75.1e-28 # Iridium
quadrupoleListAll["197Au"] = 54.7e-28 # Gold
quadrupoleListAll["201Hg"] = 38.6e-28 # Mercury
quadrupoleListAll["209Bi"] = -51.6e-28 # Bismuth

# Lanthanoids
quadrupoleListAll["141Pr"] = -5.89e-28 # Praseodymium
quadrupoleListAll["143Nd"] = -63.0e-28 # Neodymium
quadrupoleListAll["145Nd"] = -33.0e-28 # Neodymium
quadrupoleListAll["147Sm"] = -25.9e-28 # Samarium
quadrupoleListAll["149Sm"] = 7.4e-28 # Samarium
quadrupoleListAll["151Eu"] = 90.3e-28 # Europium
quadrupoleListAll["153Eu"] = 241.2e-28 # Europium
quadrupoleListAll["155Gd"] = 127.0e-28 # Gadolinium
quadrupoleListAll["157Gd"] = 135.0e-28 # Gadolinium
quadrupoleListAll["159Tb"] = 143.2e-28 # Terbium
quadrupoleListAll["161Dy"] = 250.7e-28 # Dysprosium
quadrupoleListAll["163Dy"] = 264.8e-28 # Dysprosium
quadrupoleListAll["165Ho"] = 358.0e-28 # Holmium
quadrupoleListAll["167Er"] = 356.5e-28 # Erbium
quadrupoleListAll["173Yb"] = 280.0e-28 # Ytterbium
quadrupoleListAll["175Lu"] = 349.0e-28 # Lutetium
quadrupoleListAll["176Lu"] = 497.0e-28 # Lutetium
quadrupoleListAll["235U"] = 493.6e-28 # Uranium


def quadrupole(nucleus):
    """
    Get the quadrupole moment of a nucleus with spin > 1/2.

    Args:
        nucleus: String describing the nucleus, e.g. "2H" or "17O".

    Returns:
        Quadrupole moment encoded as a Float, e.g. 0.5 
    """
    assert nucleus in quadrupoleListAll.keys(), "Nucleus not valid."
    return quadrupoleListAll[nucleus]

if __name__ == "__main__":
    print(spin.__doc__)
