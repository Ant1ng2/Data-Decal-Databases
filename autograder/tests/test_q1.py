import database_util
import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from HiddenPrints import HiddenPrints
with HiddenPrints():
    import SQLLab
import sqlite3 as sqlite
import os

class q1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            os.remove('database.db')
        except:
            pass

    def setUp(self):
        self.con = sqlite.connect('database.db')
        self.cur = self.con.cursor()
        SQLLab.create_table()

    '''
    @weight(1)
    def test_correct_tables_created(self):
        """Q1: Database has only a table 'ids'"""
        self.cur.execute("""SELECT name FROM sqlite_master WHERE type='table'""")
        results = self.cur.fetchall()
        self.assertEqual(len(self.cur.fetchall()), 1, 'Not the right number of tables')
        self.assertEqual(results[0][0], 'ids', 'Table is not named ids')
    '''

    @weight(1)
    def test_columns(self):
        """Q1: Database has correct columns"""
        self.cur.execute("""PRAGMA table_info(ids)""")
        columns = self.cur.fetchall()
        self.assertEqual(len(columns), 2, "The number of columns isn't right")
        self.cur.execute("""INSERT INTO ids VALUES(1.0, 1.0)""")
        self.cur.execute("""SELECT id, name FROM ids""")
        results = self.cur.fetchall()
        self.assertEqual(len(results), 1, 'More than one entry.')
        value = results[0]
        self.assertEqual(len(value), 2, "Two columns weren't received?")
        self.assertIsInstance(value[0], int, 'First column is not an int.')
        self.assertIsInstance(value[1], str, 'Second column is not a string.')

    @weight(1)
    def test_errors(self):
        """Q1: Table doesn't error after multiple calls"""
        try:
            SQLLab.create_table()
        except sqlite.OperationalError:
            self.fail('Threw an error after calling a multiple time')
    
    @weight(1)
    def test_no_changes(self):
        """Q1: Test no changes if table already exists"""
        self.cur.execute("INSERT INTO ids VALUES (1, '1.0')")
        self.cur.execute("PRAGMA data_version")
        version = self.cur.fetchone()
        self.test_errors()
        self.cur.execute("PRAGMA data_version")
        self.assertTupleEqual(version, self.cur.fetchone(), 'Database changed')

    def tearDown(self):
        self.con.close()
        os.remove('database.db')

if __name__ == '__main__':
    unittest.main()