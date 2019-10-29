import database_util
import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from HiddenPrints import HiddenPrints
with HiddenPrints():
    import SQLLab
import sqlite3 as sqlite
import os

class pq2(unittest.TestCase):
    def setUp(self):
        self.con = sqlite.connect("database.db")
        self.cur = self.con.cursor()
        SQLLab.hello_world()

    @weight(1)
    def test_changes_saved(self):
        """PreQ2: Changes have been saved"""
        self.cur.execute('SELECT * FROM q2')
        results = self.cur.fetchall()
        self.assertEqual(len(results), 1, 'Not the right number of entries')
        self.assertEqual(results[0], (0, 'Hello'), "Entry wasn't equal to expected")
    
    def tearDown(self):
        self.con.close()
        os.remove("database.db")

if __name__ == '__main__':
    unittest.main()