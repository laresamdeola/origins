import unittest
from player_details import is_color_lower, is_not_a_word, is_special_character


class TestColorDetails(unittest.TestCase):
#Check if the player_color_details turns upper case color inputs to all lower case
    def test_is_color_lower(self):
        self.assertEqual(is_color_lower(), "red")

# Check if the player_color_details does not accept numerical values
    def test_is_not_a_word(self):
        self.assertEqual(is_not_a_word(), False)

# Check if the player_color_details does not accept special characters
    def test_is_a_special_character(self):
        self.assertEqual(is_special_character(), True)


if __name__ == '__main__':
    unittest.main()