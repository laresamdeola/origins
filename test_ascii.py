import unittest
from ascii import is_orunmila_string, is_ogun_string, is_oshun_string, is_obatala_string, is_obaluaye_string, is_oya_string,\
is_agemo_string, is_yemoja_string, is_ibeji_string, is_sango_string, is_eshu_string


class TestAsciiDetails(unittest.TestCase):
#Check if the selected ascii art is a string
    def test_is_orunmila_a_string(self):
        self.assertTrue(is_orunmila_string(), True)

#Check if the selected ascii art is a string
    def test_is_ogun_a_string(self):
        self.assertTrue(is_ogun_string(), True)

#Check if the selected ascii art is a string
    def test_is_oshun_a_string(self):
        self.assertTrue(is_oshun_string(), True)

#Check if the selected ascii art is a string
    def test_is_obatala_a_string(self):
        self.assertTrue(is_obatala_string(), True)

#Check if the selected ascii art is a string
    def test_is_obaluaye_a_string(self):
        self.assertTrue(is_obaluaye_string(), True)

#Check if the selected ascii art is a string
    def test_is_oya_a_string(self):
        self.assertTrue(is_oya_string(), True)

#Check if the selected ascii art is a string
    def test_is_agemo_a_string(self):
        self.assertTrue(is_agemo_string(), True)

#Check if the selected ascii art is a string
    def test_is_yemoja_a_string(self):
        self.assertTrue(is_yemoja_string(), True)

#Check if the selected ascii art is a string
    def test_is_ibeji_a_string(self):
        self.assertTrue(is_ibeji_string(), True)

#Check if the selected ascii art is a string
    def test_is_sango_a_string(self):
        self.assertTrue(is_sango_string(), True)

#Check if the selected ascii art is a string
    def test_is_eshu_a_string(self):
        self.assertTrue(is_eshu_string(), True)


if __name__ == '__main__':
    unittest.main()
