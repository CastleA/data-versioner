# import typing
import unittest

import pandas as pd

from dataversioner.dataversioner import CommitTree


class TestCommitTree(unittest.TestCase):

    def setUp(self, data: pd.DataFrame):
        self.ctree = CommitTree(data)

    def tearDown(self):
        self.ctree.dispose()

    def test_init():
        pass

    def test_print():
        pass

    def test_create_committree(data: pd.DataFrame, name: str, message: str):
        pass

    def test_get_committree_str(self, verbose: bool = False) -> str:
        pass

    def test_get_all_commits(self, mode: str = 'names'):
        pass

    def test_get_current(self):
        pass

    def test_get_commit_str(self, name: str, verbose: bool = False):
        pass

    def test_get_commit_data(self, name: str, copy: bool = True):
        pass

    def test_add_commit(self, data: pd.DataFrame(), name: str, message: str):
        pass

    def test_checkout_commit(self, name: str):
        pass
