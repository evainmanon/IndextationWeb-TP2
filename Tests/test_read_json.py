import unittest
from Index.read_json import *


class TestReadJson(unittest.TestCase):
    def test_part_list(self):
        list1 = [1,2,3,4,5]
        liste_part = part_list(list1, 2)
        return self.assertEqual(liste_part,[1,2])

if __name__ == '__main__':
    unittest.main()