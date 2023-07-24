from translator import english_to_french,french_to_english
import unittest
class TestTranslator(unittest.TestCase):
    def test1_english_to_french(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french("I am Resham Chandak"),"Jius Resham Chandak")
    
    def test2_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("Jius Resham Chandak"),"I am Resham Chandak")

unittest.main()
