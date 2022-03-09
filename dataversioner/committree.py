from dataversioner.datacommit import DataCommit

import pandas as pd


class CommitTree():

    def __init__(self, data: pd.DataFrame, name: str = "Initial df", message: str = "Data at initialization") -> None:
        self.commits = {name: DataCommit(data, name, message)}
        self.successors = {name: []}
        self.root = name
        self.current = name
        self.depth = 1

    def __str__(self):

        def traverse_tree(commit_name: str, n_indent: int = 0):
            if commit_name == self.root:
                print_out = commit_name
            else:
                print_out = "\n" + " " * n_indent + "- " + commit_name
            for succ_name in self.successors[commit_name]:
                print_out += traverse_tree(succ_name, n_indent + 3)
            return print_out

        return traverse_tree(self.root)

    def verbose_ctree_str(self):

        def traverse_depth(commit_name: str):
            depths = [0]
            for succ_name in self.successors[commit_name]:
                depths.append(traverse_depth(succ_name))
            return max(max(depths) + 1, 1)
        depth = traverse_depth(self.root)

        def traverse_tree(commit_name: str, depth, n_indent: int = 0):
            
            if commit_name == self.root:
                print_out = commit_name  + "\t" * depth + self.commits[commit_name].message 
            else:
                print_out = "\n" + " " * n_indent + "- " + commit_name + "\t"  * depth + self.commits[commit_name].message 
            for succ_name in self.successors[commit_name]:
                print_out += traverse_tree(succ_name, depth - 1, n_indent + 3)
            return print_out
        return traverse_tree(self.root, depth)

    def commit_exists(self, name: str):
        return name in self.commits.keys()

    def get_commit_data(self, name:str, copy: bool = True):
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
            return list(self.commits.keys())
        elif mode == 'details':
            return [self.commits[name].get_details() for name in self.commits.keys()]

    def get_current(self):
        return self.current

    def verbose_commit_str(self, name: str):
        return str(self.commits[name]) + f"\n\n{str(self.commits[name].get_data(False))}"
        
