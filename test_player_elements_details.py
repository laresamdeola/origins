import unittest
from player_details import is_element, is_an_element_name, is_element_name_lower


class TestElementDetails(unittest.TestCase):
#Check if the selected elements is in he list of allowed elements
    def test_is_element(self):
        self.assertIs(is_element(), True)

# Check if the selected elements is not in the list of allowed elements
    def test_is_not_element(self):
        self.assertIsNot(is_element(), True)

# Check if the player_element_details accepts numerical values or not
    def test_is_an_element_name(self):
        self.assertIs(is_an_element_name(), False)

# Check if the player_element_details accepts numerical values or not
    def test_is_an_element_name_lower(self):
        self.assertEqual(is_element_name_lower(), False)


if __name__ == '__main__':
    unittest.main()
