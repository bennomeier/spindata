""" This module contains the total spin for all the nuclei and the electron.

Based on  

R. K. Harris et al., NMR nomenclature. Nuclear spin properties and conventions for chemical shifts(IUPAC Recommendations 2001) 
Pure Appl. Chem., Vol. 73, No. 11, pp. 1795-1818, 2001.
https://doi.org/10.1351/pac200173111795

The values are stored in the dictionary spinListAll.

The function spin(nuc) will return the spin of nucleus nuc, which is specified e.g. as "1H"
"""

spinListAll = {}
spinListAll["E"] = 1./2

#Spin 1/2 Isotopes
spinListAll["1H"] = 1./2 # H
spinListAll["3He"] = 1./2 # Helium
spinListAll["13C"] = 1./2 # Carbon
spinListAll["15N"] = 1./2 # Nitrogen
spinListAll["19F"] = 1./2 # Fluor
spinListAll["29Si"] = 1./2 # Si
spinListAll["31P"] = 1./2 # Phosphor
spinListAll["57Fe"] = 1./2 # Iron
spinListAll["77Se"] = 1./2 # Selenium
spinListAll["89Y"] = 1./2 # Yttrium
spinListAll["103Rh"] = 1./2 # Rhodium
spinListAll["107Ag"] = 1./2 # Silver
spinListAll["109Ag"] = 1./2 # Silver
spinListAll["111Cd"] = 1./2 # Cadmium, not preferred
spinListAll["115Sn"] = 1./2 # Tin
spinListAll["117Sn"] = 1./2 # Tin
spinListAll["119Sn"] = 1./2 # Tin
spinListAll["123Te"] = 1./2 # Tellurium
spinListAll["125Te"] = 1./2 # Tellur
spinListAll["129Xe"] = 1./2 # Xenon
spinListAll["183W"] = 1./2 # Tungsten
spinListAll["187Os"] = 1./2 # Osmium
spinListAll["195Pt"] = 1./2 # Platinum
spinListAll["199Hg"] = 1./2 # Mercury
spinListAll["203Tl"] = 1./2 # Thallium
spinListAll["205Tl"] = 1./2 # Thallium
spinListAll["207Pb"] = 1./2 # Lead

#Quadrupolar Isotopes
spinListAll["2H"] = 1. # 
spinListAll["6Li"] = 1. # Lithium
spinListAll["7Li"] = 3./2 # Lithium
spinListAll["9Be"] = 3./2 # Beryllium
spinListAll["10B"] = 3 # Boron
spinListAll["11B"] = 3./2 # Boron
spinListAll["14N"] = 1. # Nitrogen
spinListAll["17O"] = 5./2 # Oxygen
spinListAll["21Ne"] = 3./2 # Neon
spinListAll["23Na"] = 3./2 # Sodium
spinListAll["25Mg"] = 5./2 # Magnesium
spinListAll["27Al"] = 5./2 # Aluminum
spinListAll["33S"] = 3./2 # Sulphur
spinListAll["35Cl"] = 3./2 # Chlorine
spinListAll["37Cl"] = 3./2 # Chlorine
spinListAll["39K"] = 3./2 # Potassium
spinListAll["40K"] = 4 # Potassium
spinListAll["41K"] = 3./2 # Potassium
spinListAll["43Ca"] = 7./2 # Calcium
spinListAll["45Sc"] = 7./2 # Scandium
spinListAll["47Ti"] = 5./2 # Titanium
spinListAll["49Ti"] = 7./2 # Titanium
spinListAll["50V"] = 6 # Vanadium
spinListAll["51V"] = 7./2 # Vanadium
spinListAll["53Cr"] = 3./2 # Chromium
spinListAll["55Mn"] = 5./2 # Manganese
spinListAll["59Co"] = 7./2 # Cobalt
spinListAll["61Ni"] = 3./2 # Nickel
spinListAll["63Cu"] = 3./2 # Copper
spinListAll["65Cu"] = 3./2 # Copper
spinListAll["67Zn"] = 5./2 # Zinc
spinListAll["69Ga"] = 3./2 # Gallium
spinListAll["71Ga"] = 3./2 # Gallium
spinListAll["73Ge"] = 9./2 # Germanium
spinListAll["75As"] = 3./2 # Arsenic
spinListAll["79Br"] = 3./2 # Bromine
spinListAll["81Br"] = 3./2 # Bromine
spinListAll["83Kr"] = 9./2 # Krypton
spinListAll["85Rb"] = 5./2 # Rubidium
spinListAll["87Rb"] = 3./2 # Rubidium
spinListAll["87Sr"] = 9./2 # Strontium
spinListAll["91Zr"] = 5./2 # Zirconium
spinListAll["93Nb"] = 9./2 # Niobium
spinListAll["95Mo"] = 5./2 # Molybdenum
spinListAll["97Mo"] = 5./2 # Molybdenum
spinListAll["99Tc"] = 9./2 # Technetium
spinListAll["99Ru"] = 5./2 # %Ruthenium
spinListAll["101Ru"] = 5./2 # Ruthenium
spinListAll["105Pd"] = 5./2 # Palladium
spinListAll["113In"] = 9./2 # Indium
spinListAll["115In"] = 9./2 # Indium
spinListAll["121Sb"] = 5./2 # Antimony
spinListAll["123Sb"] = 7./2 # Antimony
spinListAll["127I"] = 5./2 # Iodine
spinListAll["131Xe"] = 3./2 # Xenon
spinListAll["133Cs"] = 7./2 # Caesium
spinListAll["135Ba"] = 3./2 # Barium
spinListAll["137Ba"] = 3./2 # Barium
spinListAll["138La"] = 5 # Lanthanum
spinListAll["139La"] = 7./2 # Lanthanum
spinListAll["177Hf"] = 7./2 # Hafnium
spinListAll["179Hf"] = 9. # Hafnium
spinListAll["181Ta"] = 7./2 # Tantalum
spinListAll["185Re"] = 5./2 # Rhenium
spinListAll["187Re"] = 5./2 # Rhenium
spinListAll["189Os"] = 3./2 # Osmium
spinListAll["191Ir"] = 3./2 # Iridium
spinListAll["193Ir"] = 3./2 # Iridium
spinListAll["197Au"] = 3./2 # Gold
spinListAll["201Hg"] = 3./2 # Mercury
spinListAll["209Bi"] = 9./2 # Bismuth

# Lanthanoids
spinListAll["141Pr"] = 5./2 # Praseodymium
spinListAll["143Nd"] = 7./2 # Neodymium
spinListAll["145Nd"] = 7./2 # Neodymium
spinListAll["147Sm"] = 7./2 # Samarium
spinListAll["149Sm"] = 7./2 # Samarium
spinListAll["151Eu"] = 5./2 # Europium
spinListAll["153Eu"] = 5./2 # Europium
spinListAll["155Gd"] = 3./2 # Gadolinium
spinListAll["157Gd"] = 3./2 # Gadolinium
spinListAll["159Tb"] = 3./2 # Terbium
spinListAll["161Dy"] = 5./2 # Dysprosium
spinListAll["163Dy"] = 5./2 # Dysprosium
spinListAll["165Ho"] = 7./2 # Holmium
spinListAll["167Er"] = 7./2 # Erbium
spinListAll["173Yb"] = 5./2 # Ytterbium
spinListAll["175Lu"] = 7./2 # Lutetium
spinListAll["176Lu"] = 7. # Lutetium
spinListAll["235U"] = 7./2 # Uranium

def spin(nucleus):
    """
    Get the spin of a given nucleus.

    Args:
        nucleus: String describing the nucleus, e.g. "13C", "1H" or "E" for the electron.

    Returns:
        Spin encoded as a Float, e.g. 0.5 
    """
    assert nucleus in spinListAll.keys(), "Nucleus not valid."
    return spinListAll[nucleus]

if __name__ == "__main__":
    print(spin.__doc__)
