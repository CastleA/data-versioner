from typing import List

import pandas as pd

from datacommit import DataCommit


class CommitTree():
    """The CommitTree class is a tree data structure of DataCommit objects."""
    def __init__(self, data: pd.DataFrame, name: str, message: str) -> None:
        self.commits = {name: DataCommit(data, name, message)}
        self.successors = {name: []}
        self.root = name
        self.current = name

    def __str__(self):
        return self.get_committree_str()

    def _traverse_tree(self, commit_name: str, depth: int = 0):
        details = self.commits[commit_name].get_details()
        tree_list = [{'depth': depth, **details}]
        for succ_name in self.successors[commit_name]:
            tree_list += self._traverse_tree(succ_name, depth + 1)
        return tree_list

    def get_committree_str(self, verbose: bool = False) -> str:
        string = ""
        traversed_tree = self._traverse_tree(self.root)

        if verbose:
            message_justify = max([c['depth']*5 + len(c['name']) for c in traversed_tree]) + 8
            for node in traversed_tree:
                leading = '' if node['depth'] == 0 else ' ' * ((node['depth'] * 5) - 2) + '- '
                padded_name = node['name'].ljust(message_justify - node['depth'] * 5)
                string += '{}{}{}\n'.format(leading, padded_name, node['message'])
        else:
            for node in traversed_tree:
                width = (node['depth'] - 1) * 5 + 3
                string += '{}{}{}\n'.format(' ' * width, '- ' if node['depth'] else '', node['name'])

        return string

    def _get_all_commits(self) -> List[str]:
        return list(self.successors.keys())

    def get_all_commits(self, mode: str = 'names'):
        if mode == 'names':
            return self._get_all_commits()
        elif mode == 'details':
            return [self.commits[name].get_details() for name in self._get_all_commits()]

    def _get_successors(self, name: str) -> List[str]:
        return self.successors[name]

    def get_current(self):
        return self.current

    def get_commit_str(self, name: str, verbose: bool = False):
        if verbose:
            return str(self.commits[name]) + f"\n\n{str(self.commits[name].get_data(False))}"
        else:
            return str(self.commits[name])

    def get_commit_data(self, name: str, copy: bool = True):
        return self.commits[name].get_data(copy)

    def add_commit(self, data: pd.DataFrame(), name: str, message: str):
        self.commits[name] = DataCommit(data.copy(), name, message)
        self.successors[self.current].append(name)
        self.successors[name] = []
        self.current = name

    def checkout_commit(self, name: str):
        self.current = name
        return self.get_commit_data(name)
