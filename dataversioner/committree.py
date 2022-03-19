from copy import deepcopy
from datetime import datetime
from typing import Dict, List


class CommitTree():
    """The CommitTree class is a tree data structure of DataCommit objects."""

    class DataCommit():
        """The DataCommit class captures a record of data along with accessory information."""
        def __init__(self, data, name: str, message: str) -> None:
            self.data = data
            self.name = name
            self.message = message
            self.commit_time = datetime.now()

        def __str__(self, trunc_len: int = 80) -> str:
            truncate = len(self.message) >= trunc_len
            message = self.message[:50] + '...' if truncate else self.message
            time_format = self.commit_time.strftime('%I:%m %p on %b %d, %Y')
            return f"'{self.name}' - {message}\nCommitted at {time_format}"

        def get_details(self) -> Dict:
            time_format = self.commit_time.strftime('%b %d, %Y %I:%m %p')
            return {
                    'name': self.name,
                    'message': self.message,
                    'time': time_format
                    }

        def get_data(self, copy: bool = True):
            if copy:
                return deepcopy(self.data)
            else:
                return self.data

    def __init__(self, commits: Dict, successors: Dict, root: str, current: str) -> None:
        self._commits = commits
        self._successors = successors
        self._root = root
        self._current = current

    def create_committree(data, name: str, message: str):
        commits = {name: CommitTree.DataCommit(data, name, message)}
        successors = {name: []}
        return CommitTree(commits, successors, name, name)

    def __str__(self):
        return self.get_committree_str()

    def _get_commits(self) -> List[str]:
        return list(self._successors.keys())

    def _get_successors(self, name: str) -> List[str]:
        return self._successors[name]

    def _traverse_tree(self, name: str, depth: int = 0):
        details = self._commits[name].get_details()
        tree_list = [{'depth': depth, **details}]
        for succ_name in self._successors[name]:
            tree_list += self._traverse_tree(succ_name, depth + 1)
        return tree_list

    def get_committree_str(self, verbose: bool = False) -> str:
        string = ""
        traversed_tree = self._traverse_tree(self._root)

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

    def get_commits(self, mode: str = 'names'):
        if mode == 'names':
            return self._get_commits()
        elif mode == 'details':
            return [self._commits[name].get_details() for name in self._get_commits()]

    def get_current(self):
        return self._current

    def get_commit_str(self, name: str, verbose: bool = True):
        if verbose:
            return str(self._commits[name]) + f"\n\n{str(self._commits[name].get_data(False))}"
        else:
            return str(self._commits[name])

    def get_commit_data(self, name: str, copy: bool = True):
        return self._commits[name].get_data(copy)

    def add_commit(self, data, name: str, message: str):
        self._commits[name] = CommitTree.DataCommit(deepcopy(data), name, message)
        self._successors[self._current].append(name)
        self._successors[name] = []
        self._current = name

    def checkout_commit(self, name: str):
        self._current = name
        return self.get_commit_data(name)
