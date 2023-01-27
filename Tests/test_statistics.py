import unittest

from Index.statistics import *

class TestStatistics(unittest.TestCase):

    def test_number_docs(self):
        liste = [1,2,3,4,5]
        nb_docs = number_docs(liste)
        return self.assertEquals(5, nb_docs)
    
    def test_number_token(self):
        token = {"Essai": 1, "Fonction": 14}
        nb_token = number_token(token)
        return self.assertEquals(2, nb_token)

    def test_mean_token(self):
        token = {"Essai": 1, "Fonction": 14}
        liste = [1,2,3]
        mean = mean_token(token, liste)
        return self.assertEquals(2/3, mean)


if __name__ == '__main__':
    unittest.main()