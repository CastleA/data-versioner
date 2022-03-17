import pandas as pd

from committree import CommitTree


class DataVersioner():

    def __init__(self, data: pd.DataFrame,
                 first_commit_name: str = "Initial df",
                 first_commit_message: str = "First commit of data") -> None:
        self.ctree = CommitTree(data.copy(),
                                first_commit_name,
                                first_commit_message)
        self.data = data

    def commit_exists(self, name: str):
        return name in self.ctree.get_all_commits()

    def commit(self, name: str, message: str):
        if self.commit_exists(name):
            raise ValueError(f"Commit '{name}' already exists. Commit names must be unique.")
        self.ctree.add_commit(self.data, name, message)

    def _data_differs_from(self, name: str):
        return not self.data.equals(self.ctree.get_commit_data(name, copy=False))

    def checkout(self, name: str, allow_discard_changes: bool = False):
        if not self.commit_exists(name):
            raise KeyError(f"Commit {name} does not exist.")

        if (not allow_discard_changes) and (self._data_differs_from(self.ctree.get_current())):
            raise ValueError("Cannot checkout while data has uncommitted changes and allow_discard_changes is False.")

        self.data = self.ctree.checkout_commit(name)

    def commits(self, verbose: bool = False):
        mode = 'details' if verbose else 'names'
        return self.ctree.get_all_commits(mode)

    def show_commits(self, verbose: bool = False):
        if verbose:
            print(self.ctree.verbose_ctree_str())
        else:
            print(self.ctree)

    def status(self):
        self.show_commit()

    def show_commit(self, name: str = None):
        if name is None:
            print(self.ctree.verbose_commit_str(self.ctree.get_current()))
        elif not self.commit_exists(name):
            raise KeyError(f"Commit {name} does not exist.")
        else:
            print(self.ctree.verbose_commit_str(name))
