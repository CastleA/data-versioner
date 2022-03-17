from typing import List

import pandas as pd

from datacommit import DataCommit


class CommitTree():

    def __init__(self, data: pd.DataFrame, name: str = "Initial df", message: str = "Data at initialization") -> None:
        self.commits = {name: DataCommit(data, name, message)}
        self.successors = {name: []}
        self.root = name
        self.current = name

    def _traverse_tree(self, commit_name: str, depth: int = 0):
        details = self.commits[commit_name].get_details()
        tree_list = [{'depth': depth, **details}]
        for succ_name in self.successors[commit_name]:
            tree_list += self._traverse_tree(succ_name, depth + 1)
        return tree_list

    def __str__(self):
        string = ""
        for node in self._traverse_tree(self.root):
            width = (node['depth'] - 1) * 5 + 3
            string += '{}{}{}\n'.format(' ' * width, '- ' if node['depth'] else '', node['name'])
        return string

    def verbose_ctree_str(self) -> str:
        string = ""
        traversed_tree = self._traverse_tree(self.root)
        message_justify = max([c['depth']*5 + len(c['name']) for c in traversed_tree]) + 8
        for node in self._traverse_tree(self.root):
            leading = '' if node['depth'] == 0 else ' ' * ((node['depth'] * 5) - 2) + '- '
            padded_name = node['name'].ljust(message_justify - node['depth'] * 5)
            string += '{}{}{}\n'.format(leading, padded_name, node['message'])
        return string

    def _get_all_commits(self) -> List[str]:
        return list(self.successors.keys())

    def _get_successors(self, name: str) -> List[str]:
        return self.successors[name]

    def get_current(self):
        return self.current

    def verbose_commit_str(self, name: str):
        return str(self.commits[name]) + f"\n\n{str(self.commits[name].get_data(False))}"

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

    def get_all_commits(self, mode: str = 'names'):
        if mode == 'names':
            return self._get_all_commits()
        elif mode == 'details':
            return [self.commits[name].get_details() for name in self.commits.keys()]
