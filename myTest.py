import unittest
import Ex1

class myTest(unittest.TestCase):

    def test_allocateAnElevsToCalls(self):
        """
        Checks if all correct
        """
        Ex1.allocateAnElevsToCalls("/Users/user/Downloads/Ex1-main-5/B2.json", "/Users/user/Downloads/Ex1-main-5/Calls_a.csv", "out.csv")
        c_list = Ex1.LoadCallsFromCsv("/Users/user/Downloads/Ex1-main-5/out.csv")
        self.assertTrue(c_list.getCalls()[0].get_allc(), 1)

    def test_LoadCallsFromCsv(self):
        """
        Checks if function LoadCallsFromCsv works correctly and loads calls from csv to class Calls_List for real
        """
        c_list = Ex1.LoadCallsFromCsv("/Users/user/Downloads/Ex1-main-5/Calls_d.csv")
        self.assertEqual(c_list.getCalls()[0].get_source(), -7)
    def test_check(self):
        self.assertEqual(5, 5)


if __name__ == '__main__':
    unittest.main()