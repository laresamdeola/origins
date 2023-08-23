import unittest
from origins_keys import is_game_info_int, is_game_info_str, is_translate_lower, is_translate_mix_characters,\
    is_translate_with_numbers, is_tales_lower, is_tales_mix_characters, is_tales_with_numbers


class TestKeysDetails(unittest.TestCase):
#Check if the game info key returns an int
    def test_is_game_info_int(self):
        self.assertEqual(is_game_info_int(), True)

# Check if game info returns a string
    def test_is_game_info_str(self):
        self.assertIsNot(is_game_info_str(), True)

# Check if the translate input returns lower case letters
    def test_is_translate_lower(self):
        self.assertEqual(is_translate_lower(), "aaron")

# Check if the translate input returns mixed case letters as all lower case
    def test_is_translate_mix_characters(self):
        self.assertEqual(is_translate_mix_characters(), "jeanette")

#Check if the translate input accepts numbers
    def test_is_translate_with_numbers(self):
        self.assertNotEqual(is_translate_with_numbers(), "jeanette")

# Check if the tales input function turns all uppercase letters to lower case
    def test_is_tales_lower(self):
        self.assertEqual(is_tales_lower(), "amrit")

# Check if the tales input function turns mixed case letters to all lower case letters
    def test_is_tales_mix_characters(self):
        self.assertIs(is_tales_mix_characters(), False)

# Check if the tales input function accepts numerical values
    def test_is_tales_with_numbers(self):
        self.assertEqual(is_tales_with_numbers(), True)


if __name__ == '__main__':
    unittest.main()
