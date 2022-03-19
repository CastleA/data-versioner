from typing import Optional

import pandas as pd

from dataversioner.committree import CommitTree


class DataVersioner():
    """The DataVersioner class is the interface between the user and the CommitTree tree object."""

    def __init__(self, data: pd.DataFrame,
                 name: str = "Initial dataframe", message: str = "Data at initialization") -> None:
        self.ctree = CommitTree.create_committree(data.copy(), name, message)
        self.data = data

    def commit_exists(self, name: str):
        return name in self.ctree.get_commits()

    def commit(self, name: str, message: str, data: Optional[pd.DataFrame]):
        if self.commit_exists(name):
            raise ValueError(f"Commit '{name}' already exists. Commit names must be unique.")
        if data is None:
            self.ctree.add_commit(self.data, name, message)
        else:
            self.ctree.add_commit(data, name, message)
            self.data = data

    def _data_differs(self, df1: pd.DataFrame, df2: pd.DataFrame):
        return not df1.equals(df2)

    def checkout(self, name: str, protect_changes: bool = True):
        if not self.commit_exists(name):
            raise KeyError(f"Commit {name} does not exist.")
        if protect_changes:
            if self._data_differs(self.data, self.ctree.get_commit_data(self._ctree.get_current(), copy=False)):
                raise ValueError("Cannot checkout while data has uncommitted changes and protect_changes is True.")
        self.data = self.ctree.checkout_commit(name)

    def commits(self, verbose: bool = False):
        mode = 'details' if verbose else 'names'
        return self.ctree.get_commits(mode)

    def show_commits(self, verbose: bool = False):
        print(self.ctree.get_committree_str(verbose=verbose))

    def status(self):
        self.show_commit()

    def show_commit(self, name: str = None):
        if name is None:
            print(self.ctree.get_commit_str(self.ctree.get_current()))
        elif not self.commit_exists(name):
            raise KeyError(f"Commit {name} does not exist.")
        else:
            print(self.ctree.get_commit_str(name))
