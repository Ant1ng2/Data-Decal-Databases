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
        """Q4: Function called on an empty table"""
        self.assertEqual(len(SQLLab.field_popularity()), 0)
    '''

    @weight(3)
    def test_q4(self):
        """Q4: Main function"""
        database_util.testDatabase()
        self.assertEqual(SQLLab.field_popularity(), 
            [(1, 'Engineering'), (1, 'Investments'), (2, 'HR'), (2, 'IT'), (2, 'Sales')])

    def tearDown(self):
        self.con.close()
        os.remove('database.db')

if __name__ == '__main__':
    unittest.main()