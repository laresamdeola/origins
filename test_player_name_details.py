import unittest
from player_details import is_lower, not_number


class TestPlayerDetails(unittest.TestCase):
#To check if the player_name_details function accepts an input strin in title case and returns that string lower case
    def test_upper_case(self):
        self.assertEqual(is_lower(), "matilda")

# Check if a player_name_details function accepts a mixed case string and converts to lower case string
    def test_mixed_case(self):
        self.assertEqual(is_lower(), "amrit")

# Check if a player_name_details function accepts a mixed case string and converts to lower case string
    def test_handle_space(self):
        self.assertEqual(is_lower(), "wenjia")

# Check if the player_name_details function can handle numbers
    def test_handle_numbers(self):
        self.assertIs(not_number(), False)

# Check if the player_name_details function can handle numbers
    def test_numbers_mix(self):
        self.assertIs(not_number(), False)


if __name__ == '__main__':
    unittest.main()
