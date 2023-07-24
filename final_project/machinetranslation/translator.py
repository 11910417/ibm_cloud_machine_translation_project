"""
Using deep_translator, we are importing MyMemoryTranslator method.
 Here, we are performing machine translation.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(englishtext):
    """
    Converting English to French.
    """
    frenchtext=MyMemoryTranslator(source='en-IN',target='fr-FR').translate(text=englishtext)
    return frenchtext

def french_to_english(frenchtext):
    """
    Converting French to English.
    """
    englishtext=MyMemoryTranslator(source='fr-FR',target='en-IN').translate(text=frenchtext)
    return englishtext
    