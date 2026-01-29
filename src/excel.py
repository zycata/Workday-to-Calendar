import pandas as pd
import numpy as np
import warnings
from typing import List
# Filter out the specific openpyxl UserWarning
warnings.filterwarnings("ignore", category=UserWarning, module='openpyxl')

from pprint import pprint

class Workday_Schedule:
    first_col_name: str = "start"
    cols_to_drop = [first_col_name, "drop", "swap", "credits", "grading basis", "instructional format", "delivery mode"]
    
    def __init__(self, df: pd.DataFrame):
        self.schedule_data = df
        pass

    @classmethod
    def read_workday_excel(self, file_path:str, skip_rows: int):
        df: pd.DataFrame = pd.read_excel(file_path, skiprows=skip_rows)
        df.columns = df.columns.str.lower()
        df.columns.values[0] = self.first_col_name
        for col_name in self.cols_to_drop:
            try:
                df = df.drop(col_name, axis=1)
            except KeyError:
                print(col_name, "does not exist, skipping")
        return self(df)
    
    def __getitem__(self, key: List[str]):
        return self.schedule_data[key]

    # returns list like structure
    def get_column_names(self):
        return self.schedule_data.columns
        

    def clean_data(self, df: pd.DataFrame = None) -> None:
        # has to be a better way to do that right
        if df is None:
            df = self.schedule_data
        # this code is so bad that ai could never
        df["section"] = df["section"].apply(lambda s: s.split(" ")[1])
        df = df[df['registration status'] == 'Registered']

    def get_list_of_row(self, row_num: int) -> list:
        dataframe = self.schedule_data
        list = []
        data_row = dataframe.iloc[row_num]
        # print("-------print col info--------")
        for name, datapoint in data_row.items():
            # print(f"{name} :  {datapoint}")
            if (datapoint is np.nan):
                # print("is nan omg")
                list.append("n/a")
            else:
                list.append(datapoint)
        return list





workday_s = Workday_Schedule.read_workday_excel("View_My_Courses.xlsx", 2)

workday_s.clean_data()

pprint(workday_s.get_list_of_row(4))
pprint(workday_s[['section']])
print(workday_s.get_column_names())