from chem import Element, Molecule

def test_setup():
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

def test_split_polyatomic():
    """Sees if the program can split formula with parentheses for polyatomic ions into the intended lists of chunks."""

test_setup()