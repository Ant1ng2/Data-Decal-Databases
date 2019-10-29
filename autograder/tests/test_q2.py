import database_util
import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from HiddenPrints import HiddenPrints
with HiddenPrints():
    import SQLLab
import sqlite3 as sqlite
import os

class q2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            os.remove('database.db')
        except:
            pass

    def setUp(self):
        self.con = sqlite.connect('database.db')
        self.cur = self.con.cursor()

    @weight(1)
    def test_empty(self):
        """Q2: Function called on an empty database"""
        SQLLab.populate_table()
        self.cur.execute("""SELECT * FROM ids""")
        self.assertListEqual(self.cur.fetchall(), 
            [(1, 'Oski'), (2, 'Is'), (3, 'The'), (4, 'Best')],
            'Entries do not equal to expected')

    @weight(1)
    def test_existing_1(self):
        """Q2: Function called with table ids existing (1)"""
        SQLLab.populate_table()
        self.test_empty()

    @weight(1)
    def test_existing_2(self):
        """Q2: Function called with table ids existing (2)"""
        self.cur.execute('CREATE TABLE ids (name TEXT)')
        self.cur.execute("INSERT INTO ids VALUES ('hello')")
        self.con.commit()
        SQLLab.populate_table()
        self.test_empty()
    
    '''
    @weight(1)
    def test_other_table(self):
        """Q2: Function called with other table existing (3)"""
        self.cur.execute('CREATE TABLE test (id)')
        self.cur.execute('INSERT INTO test VALUES (1)')
        self.con.commit()
        SQLLab.populate_table()
        self.test_empty()
        self.cur.execute('SELECT * FROM test')
        results = self.cur.fetchall()
        self.assertEqual(len(results), 1, "Number of entries doesn't match")
        self.assertEqual(results[0][0], 1, "Entry was changed")
    '''
    
    def tearDown(self):
        self.con.close()
        os.remove('database.db')

if __name__ == '__main__':
    unittest.main()