import database_util
import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from HiddenPrints import HiddenPrints
with HiddenPrints():
    import SQLLab
import sqlite3 as sqlite

class pq1(unittest.TestCase):
    def setUp(self):
        pass

    @weight(1)
    def test_cursor_uses_same_connection(self):
        """PreQ1: Cursor uses the same connection"""
        con, cur = SQLLab.open_new_connection(':memory:')
        self.assertEqual(con, cur.connection, "Cursor doesn't share the same connection")

if __name__ == '__main__':
    unittest.main()