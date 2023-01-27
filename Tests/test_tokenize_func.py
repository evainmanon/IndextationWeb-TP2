import unittest

from Index.tokenize_func import *

class TestReadJson(unittest.TestCase):
    
    def test_list_word(self):
        title = ["Test de la fonction list_word"]
        liste_word = list_word(title)
        liste_word_expected = ["Test", "de", "la", "fonction", "list_word"]
        return self.assertEquals(liste_word, liste_word_expected)

    def test_search_word1(self):
        word = "de"
        word_title = ["Test de la fonction list_word"]
        ind = search_word_1(word, word_title)
        return self.assertEquals(1, ind)

if __name__ == '__main__':
    unittest.main()