import unittest
from player_details import is_metal_lower, is_metal, is_a_metal_name


class TestMetalDetails(unittest.TestCase):
#Check if the inputed metal turns upper case letters to lower case
    def test_is_metal_lower(self):
        self.assertEqual(is_metal_lower(), "diamond")

# Check if the selected metal is not in the list of metals(precious_metals)
    def test_is_metal(self):
        self.assertIs(is_metal(), True)

# Check if the player_metal_details accepts numerical values or not
    def test_is_a_metal_name(self):
        self.assertEqual(is_a_metal_name(), True)


if __name__ == '__main__':
    unittest.main()