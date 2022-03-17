# import typing
import unittest

import pandas as pd

from dataversioner.dataversioner import CommitTree


class TestCommitTree(unittest.TestCase):

    def setUp(self, data: pd.DataFrame):
        self.ctree = CommitTree(data)

    def tearDown(self):
        self.ctree.dispose()

    def test_init_committree():
        pass
