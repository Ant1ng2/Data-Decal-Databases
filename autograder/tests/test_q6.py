import database_util
import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from HiddenPrints import HiddenPrints
with HiddenPrints():
    import SQLLab
import sqlite3 as sqlite
import os
import pandas as pd

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
        database_util.testDatabase()

    @weight(6)
    def test_q6a(self):
        """Q6a: Main function"""
        self.cur.execute(SQLLab.full_outer_join())
        self.assertListEqual(self.cur.fetchall(),
            [(0, 'Harry', 'Truman', None, None),
            (1, 'John', 'Doe', None, None),
            (2, 'Rachel', 'Green', None, None),
            (3, 'Ross', 'Geller', None, None),
            (4, 'John', 'Cena', 'Cant C.', 'Mei'),
            (5, 'Jonathan', 'Joestar', 'Will', 'Zeppeli'),
            (6, 'Sherlock', 'Holmes', 'Inspector', 'Lestrade'),
            (7, 'John', 'Watson', 'Sherlock', 'Holmes'),
            (8, None, None, 'Oski', 'Bear'),
            (9, None, None, 'John', 'Hammond'),
            (10, None, None, 'Richard', 'Feynman'),
            (11, None, None, 'George', 'Lucas')])
    
    @weight(1)
    def test_q6b(self):
        """Q6b: Main function"""
        self.assertTrue(SQLLab.full_outer_join_df().equals(pd.read_sql(SQLLab.full_outer_join(), self.con)))

    def tearDown(self):
        self.con.close()
        os.remove('database.db')

if __name__ == '__main__':
    unittest.main()