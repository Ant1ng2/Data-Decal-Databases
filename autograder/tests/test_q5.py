import database_util
import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from HiddenPrints import HiddenPrints
with HiddenPrints():
    import SQLLab
import sqlite3 as sqlite
import os

class q3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            os.remove('database.db')
        except:
            pass

    def setUp(self):
        self.con = sqlite.connect('database.db')
        self.cur = self.con.cursor()
        database_util.initialize_tables()

    '''
    @weight(1)
    def test_empty(self):
        """Q5: Function called on an empty table"""
        self.assertEqual(len(SQLLab.max_salary_title()), 0)
    '''

    @weight(4)
    def test_q5(self):
        """Q5: Main function"""
        database_util.testDatabase()
        self.assertListEqual(SQLLab.max_salary_title(), 
            [(4, 'John', 'Cena', 'Sales', 100.01),
            (2, 'Rachel', 'Green', 'HR', 50.0),
            (3, 'Ross', 'Geller', 'IT', 49.99),
            (7, 'John', 'Watson', 'Investments', 39.0),
            (0, 'Harry', 'Truman', 'Engineering', 17.1)])

    def tearDown(self):
        self.con.close()
        os.remove('database.db')

if __name__ == '__main__':
    unittest.main()