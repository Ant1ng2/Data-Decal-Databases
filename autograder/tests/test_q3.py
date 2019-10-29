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
        """Q3: Function called on an empty table"""
        self.assertEqual(len(SQLLab.find_john()), 0)
    '''

    @weight(3)
    def test_q3(self):
        """Q3: Main function"""
        database_util.testDatabase()
        self.assertEqual(SQLLab.find_john(), 
            [(1, 'John', 'Doe'), (4, 'John', 'Cena'), (7, 'John', 'Watson')])

    def tearDown(self):
        self.con.close()
        os.remove('database.db')

if __name__ == '__main__':
    unittest.main()