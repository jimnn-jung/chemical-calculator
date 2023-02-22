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
        return Element.mass_dictionary[self.symbol]
    
    def set_mass(self, new_mass):
        """Setter method that allows the user to change the mass."""
        Element.mass_dictionary[self.symbol] = new_mass

# The class representing chemical molecules and compounds. Elements in the compounds must be instantiated before the compound itself.
class Molecule:

    def __init__(self, formula):
        self.formula = formula
        self.composition = self.decompose_formula()
        self.molar_mass = self.calculate_molar_mass()

    def get_formula(self):
        """Getter method of a Molecule's formula."""
        return self.formula

    def get_composition(self):
        """Getter method of a Molecule's composition."""
        return self.composition

    def get_molar_mass(self):
        """Getter method of a Molecule's molar mass."""
        return self.molar_mass

    def calculate_molar_mass(self):
        """Calculates the molar mass with helper methods."""
        composition_dict = self.get_composition()
        mass = 0
        for elem in composition_dict:
            mass += Element.mass_dictionary[elem] * composition_dict[elem]
        return mass

    def decompose_formula(self):
        """Given the list from split_formula, organizes the chemical formula into a dictionary with Element symbols as keys and the counts as values."""
        split_list = self.split_formula()
        composition = {}
        for chunk in split_list:
            num = re.search(r"\d+", chunk)
            if num:
                factor = int(num.group())
            else:
                factor = 1
            elem = re.search(r"([A-Z][a-z]*)", chunk).group()
            composition[elem] = composition.get(elem, 0) + factor
        return composition

    def split_formula(self):
        """Given the chemical formula, returns a list of chunks an Element and its count using RegEx."""
        formula_copy = self.get_formula()
        chunks = []
        open_paren = re.findall(r"\(", formula_copy)
        close_paren = re.findall(r"\)", formula_copy)
        if len(open_paren) != len(close_paren):
            raise Exception("Unmatching numbers of opening and closing parentheses")
        for i in range(len(open_paren)):
            polyatomic = re.search(r"\(([A-Z][a-z]?\d*)+\)\d+", formula_copy)
            if not polyatomic:
                raise Exception("Invalid polyatomic group in provided formula")
            poly_group = polyatomic.group()
            closing = poly_group.index(")")
            factor = int(poly_group[(closing + 1):])
            chunks.extend(re.findall(r"([A-Z][a-z]?\d*)", poly_group) * factor)
            first_opening = formula_copy.index("(")
            formula_copy = formula_copy[:first_opening] + formula_copy[(first_opening + len(poly_group)):]
        chunks.extend(re.findall(r"([A-Z][a-z]?\d*)", formula_copy))
        return chunks

    def get_mass_composition(self, symbol):
        """Calculates mass composition of symbol in the Moleculem, in percentage. The symbol must be a valid one of an Element that makes up this Molecule."""
        comp_copy = self.get_composition()
        return round(comp_copy[symbol] * Element.mass_dictionary[symbol] / self.get_molar_mass(), 4) * 100
