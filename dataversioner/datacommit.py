from datetime import datetime
from typing import Dict

import pandas as pd


class DataCommit():

    def __init__(self, data: pd.DataFrame, name: str, message: str) -> None:
        self.df = data
        self.name = name
        self.message = message
        self.commit_time = datetime.now()

    def __str__(self) -> str:
        truncate = len(self.message) >= 50
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

    def get_data(self, copy: bool = True) -> pd.DataFrame:
        if copy:
            return self.df.copy()
        else:
            return self.df
