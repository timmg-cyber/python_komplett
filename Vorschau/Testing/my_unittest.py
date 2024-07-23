import unittest

from my_module import is_even, contains_sequence

class MyUnitTest(unittest.TestCase):

##2 setUp

    def setUp(self):
        self.numbers = ((1,False),(2,True),(3,False),(4,True),(5,False),(6,True),(7,False),(8,True),(9,False),(10,True))
        print("setUp executed")

##1 main
    def test(self):
        for (i, val) in self.numbers:
            self.assertEqual(is_even(i), val)

    def tearDown(self):
        #Löschen oder Ändern von Objekten
        del self.numbers
        print("tearDown executed!")

if __name__ == '__main__':
    unittest.main()