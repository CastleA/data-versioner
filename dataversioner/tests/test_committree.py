import unittest

import pandas as pd

from dataversioner.committree import CommitTree


class TestCommitTree(unittest.TestCase):

    def setUp(self):
        name, message = "Initial dataframe", "Data at initialization"
        self.df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["a", "b", "c"])
        self.ctree = CommitTree.create_committree(self.df.copy(), name, message)

    def test_create_committree(self):
        self.df['sum'] = self.df.sum(axis=1)
        self.assertNotEqual(self.ctree.get_commit_data(self.ctree.get_current()).shape, self.df.shape)

    def test_get_committree_str(self):
        self.ctree.add_commit(self.df, 'Another commit', 'This is another commit for testing')
        self.assertEqual(self.ctree.get_committree_str(), 'Initial dataframe\n   - Another commit\n')

    def test_get_all_commits(self):
        self.assertEqual(self.ctree.get_commits(), ['Initial dataframe'])
        self.assertEqual(self.ctree.get_commits(mode='details')[0]['name'], 'Initial dataframe')
        self.assertEqual(self.ctree.get_commits(mode='details')[0]['message'], 'Data at initialization')

    def test_get_current(self):
        self.assertEqual(self.ctree.get_current(), 'Initial dataframe')

    def test_get_commit_str(self):
        commit_str = self.ctree.get_commit_str('Initial dataframe')
        self.assertTrue(commit_str.startswith("'Initial dataframe' - Data at initialization\nCommitted"))
        self.assertTrue("   a  b  c\n0  1  2  3\n1  4  5  6\n2  7  8  9" in commit_str)

    def test_get_commit_data(self):
        pass

    def test_add_commit(self):
        pass

    def test_checkout_commit(self):
        pass

    def test_get_details(self):
        pass

    def test_get_data(self):
        pass
