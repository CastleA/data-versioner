from datetime import datetime
import pandas as pd


class DataCommit():

    def __init__(self, data: pd.DataFrame, name: str, message: str) -> None:
        self.df = data
        self.name = name
        self.message = message
        self.commit_time = datetime.now()

    def __str__(self):
        text = f"'{self.name}' - {self.message if len(self.message) < 50 else self.message[:50] + '...'}"
        time = f"\nCommitted at {self.commit_time.strftime('%I:%m %p on %b %d, %Y')}"
        return text + time

    def get_details(self):
        return (self.name, self.message, self.commit_time.strftime('%b %d, %Y %I:%m %p'))

    def get_data(self, copy: bool = True):
        if copy: return self.df.copy()
        else: return self.df
         