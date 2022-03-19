import unittest

import pandas as pd

from dataversioner.dataversioner import DataVersioner


class TestDataVersioner(unittest.TestCase):

    def setUp(self):
        name, message = "Initial dataframe", "Data at initialization"
        self.df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["a", "b", "c"])
        self.dv = DataVersioner(self.df, name, message)

    def test_commit_exists(self):
        self.assertTrue(self.dv.commit_exists("Initial dataframe"))

    def test_commit(self):
        self.dv.commit('Another commit', 'This is another commit for testing')
        self.assertEqual(self.dv.commits(), ['Initial dataframe', 'Another commit'])

    def test_checkout(self):
        pass

    def test_commits(self):
        pass

    def test_show_commits(self):
        pass

    def test_status(self):
        pass

    def test_show_commit(self):
        pass
