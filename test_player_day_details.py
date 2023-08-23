import unittest
from player_details import is_day_lower, is_day, is_a_day_name


class TestDayDetails(unittest.TestCase):
#Check if the inputed day turns upper case letters to lower case
    def test_is_day_lower(self):
        self.assertEqual(is_day_lower(), "wednesday")

# Check if the selected day is not a day of the week
    def test_is_day(self):
        self.assertIs(is_day(), True)

# Check if the player_day_details accepts numerical values or not
    def test_is_a_day_name(self):
        self.assertEqual(is_a_day_name(), True)


if __name__ == '__main__':
    unittest.main()