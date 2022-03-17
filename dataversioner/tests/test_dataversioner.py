# import typing
import unittest

import pandas as pd

from dataversioner.dataversioner import DataVersioner  # , FIRST_COMMIT_NAME, FIRST_COMMIT_MESSAGE


class TestDataVersioner(unittest.TestCase):

    def setUp(self, data: pd.DataFrame):
        self.dv = DataVersioner(data)

    def tearDown(self):
        self.dv.dispose()

    def test_init():
        pass

    def test_commit_exists(self, name: str):
        pass

    def test_commit(self, name: str, message: str):
        pass

    def test_checkout(self, name: str, allow_discard_changes: bool = False):
        pass

    def test_commits(self, verbose: bool = False):
        pass

    def test_show_commits(self, verbose: bool = False):
        pass

    def test_status(self):
        pass

    def test_show_commit(self, name: str = None):
        pass
