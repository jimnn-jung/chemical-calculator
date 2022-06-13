from chem import Element, Molecule

def setup_test():
    """Instantiates a few Element objects and prints the mass_dictionary after for the Molecule class to use in tests."""
    hydrogen = Element("H", 1.01)
    oxygen = Element("O", 16.00)
    nitrogen = Element("N", 14.01)
    carbon = Element("C", 12.01)
    calcium = Element("Ca", 40.08)
    phosphate = Element("P", 94.97)
    chlorine = Element("Cl", 35.45)

    print(Element.mass_dictionary)

def test_split_simple():
    """Sees if the program can split formula into the intended lists of chunks."""
    water = Molecule("H2O")
    water_expected = ["H2", "O"]
    water_actual = water.split_formula()
    assert water_expected == water_actual, "Incorrect splitting of H2O"

    phosphoric = Molecule("H3PO4")
    phosphoric_expected = ["H3", "P", "O4"]
    phosphoric_actual = phosphoric.split_formula()
    assert phosphoric_expected == phosphoric_actual, "Incorrect splitting of H3PO4"

def test_split_polyatomic():
    """Sees if the program can split formula with parentheses for polyatomic ions into the intended lists of chunks."""
    calcium_phos = Molecule("Ca3(PO4)2")
    calcium_phos_expected = ["P", "O4", "P", "O4", "Ca3"]
    calcium_phos_actual = calcium_phos.split_formula()
    assert calcium_phos_expected == calcium_phos_actual, "Incorrect splitting of Ca3(PO4)2"

def test_decompose():
    """Checks if the program organizes the split list into a composition dictionary correctly."""
    ca_phos = Molecule("Ca3(PO4)2")
    ca_phos_expected = {"P": 2, "O": 8, "Ca": 3}
    ca_phos_actual = ca_phos.get_composition()
    assert ca_phos_expected == ca_phos_actual, "Incorrect dictionary"

def test_mass():
    """Checks if the program correctly calculates the molar mass of a Molecule."""
    water = Molecule("H2O")
    water_mass_expected = 18.02
    water_mass_actual = water.get_molar_mass()
    assert water_mass_expected == water_mass_actual, "Incorrect molar mass"

def test_mass_composition():
    """Checks if the program correctly calculates the mass composition of atoms in a Molecule."""
    acid = Molecule("HCl")
    acid_oxy_expected = round(35.45 / 36.46, 4) * 100
    print(acid_oxy_expected)
    acid_oxy_actual = acid.get_mass_composition('Cl')
    assert acid_oxy_expected == acid_oxy_actual, "Incorrect mass composition of oxygen"

setup_test()
