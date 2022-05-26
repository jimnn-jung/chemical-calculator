import re

# The class representing chemical elements. Each chemical element can be an instance object.
class Element:
    
    mass_dictionary = {}

    def __init__(self, symbol, mass):
        self.symbol = symbol
        Element.mass_dictionary[symbol] = mass

    def get_symbol(self):
        """Getter method of an Element's symbol."""
        return self.symbol

    def get_mass(self):
        """Getter method of an Element's mass."""    
        return Element.mass_dictionary[symbol]
    
    def set_mass(self, new_mass):
        """Setter method that allows the user to change the mass."""
        Element.mass_dictionary[self.symbol] = new_mass

# The class representing chemical molecules and compounds. Elements in the compounds must be instantiated before the compound itself.
class Molecule:

    def __init__(self, symbol):
        self.symbol = symbol

    def calculate_mass(self):
        """Calculates the molar mass with helper methods."""
        composition_dict = decompose_symbol()
        mass = 0
        for elem in composition_dict:
            mass += Element.mass_dictionary[elem]
        self.molar_mass = mass
        return mass

    def decompose_symbol(self):
        """Given the list from split_symbol, organizes the chemical formula into a dictionary with Element symbols as keys and the counts as values."""
        split_list = split_symbol()
        composition = {}
        # Iterate through split_list to add to dictionary
        self.composition = composition
        return composition

    def split_symbol(self):
        """Given the chemical formula, returns a list of chunks an Element and its count using RegEx."""
        symbol_copy = self.symbol
        chunks = []
        return chunks
