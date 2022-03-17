# import typing
import unittest

import pandas as pd

from dataversioner.dataversioner import DataVersioner  # , FIRST_COMMIT_NAME, FIRST_COMMIT_MESSAGE


class TestDataVersioner(unittest.TestCase):

    def setUp(self, data: pd.DataFrame):
        self.dv = DataVersioner(data)

    def tearDown(self):
        self.dv.dispose()

    def test_init_dataversioner():
        pass
