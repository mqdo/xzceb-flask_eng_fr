import unittest
import sys
sys.path.append("..")

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        with self.assertRaises(ValueError):
            french_to_english(None)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        with self.assertRaises(ValueError):
            english_to_french(None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()