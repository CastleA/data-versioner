import pandas as pd

from committree import CommitTree

FIRST_COMMIT_NAME = "Initial dataframe"
FIRST_COMMIT_MESSAGE = "Data at initialization"


class DataVersioner():
    """The DataVersioner class is the interface between the user and the CommitTree tree object."""

    def __init__(self, data: pd.DataFrame,
                 first_commit_name: str = FIRST_COMMIT_NAME,
                 first_commit_message: str = FIRST_COMMIT_MESSAGE) -> None:
        self.ctree = CommitTree.create_committree(data.copy(),
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
        print(self.ctree.get_committree_str(verbose=verbose))

    def status(self):
        self.show_commit()

    def show_commit(self, name: str = None):
        if name is None:
            print(self.ctree.get_commit_str(self.ctree.get_current()))
        elif not self.commit_exists(name):
            raise KeyError(f"Commit {name} does not exist.")
        else:
            print(self.ctree.get_committree_str(name, verbose=True))
