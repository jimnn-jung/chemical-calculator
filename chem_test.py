from chem import Element, Molecule

def setup_test():
    """Instantiates a few Element objects and prints the mass_dictionary after for the Molecule class to use in tests."""
    hydrogen = Element("H", 1.01)
    oxygen = Element("O", 16.00)
    nitrogen = Element("N", 14.01)
    carbon = Element("C", 12.01)
    calcium = Element("Ca", 40.08)
    phosphate = Element("P", 94.97)

    print(Element.mass_dictionary)

def test_split_simple():
    """Sees if the program can split formula into the intended lists of chunks."""
    water = Molecule("H2O")
    water_expected = ["H2", "O"]
    water_actual = water.split_symbol()
    assert water_expected == water_actual, "Incorrect splitting of H2O"

    phosphoric = Molecule("H3PO4")
    phosphoric_expected = ["H3", "P", "O4"]
    phosphoric_actual = phosphoric.split_symbol()
    assert phosphoric_expected == phosphoric_actual, "Incorrect splitting of H3PO4"

def test_split_polyatomic():
    """Sees if the program can split formula with parentheses for polyatomic ions into the intended lists of chunks."""

setup_test()