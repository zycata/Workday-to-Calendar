import pandas as pd
import numpy as np
import warnings
from typing import List, NamedTuple
# Filter out the specific openpyxl UserWarning
warnings.filterwarnings("ignore", category=UserWarning, module='openpyxl')

# course info file
from backend.courseinfo import Course_Info

class Workday_Schedule:
    first_col_name: str = "start"
    cols_to_drop = [first_col_name, "drop", "swap", "withdraw", "credits", "grading basis", "instructional format", "delivery mode", "start date", "end date"]
    
    def __init__(self, df: pd.DataFrame):
        self.schedule_data = df
        self.clean_data()
        pass

    @classmethod 
    # dont type hint file_path
    def read_workday_excel(cls, xlsx_file, skip_rows: int = 2):
        df: pd.DataFrame = pd.read_excel(xlsx_file, skiprows=skip_rows)
        
        return cls(df)
    
    def __getitem__(self, key: List[str]):
        return self.schedule_data[key]
    def get_item(self, row: int, key: str):
        df = self.schedule_data.iloc[row]
        return df
    # returns list like structure
    def get_column_names(self):
        return self.schedule_data.columns
        

    def clean_data(self) -> None:
        # has to be a better way to do that right
        
        df = self.schedule_data
        df.columns = df.columns.str.lower()
        df.columns.values[0] = self.first_col_name
        for col_name in self.cols_to_drop:
            try:
                df = df.drop(col_name, axis=1)
            except KeyError:
                print(col_name, "does not exist, skipping")
        # this code is so bad that ai could never
        df["course listing"] = df["course listing"].apply(lambda s: s.split(" - ")[0])
        # only keep registered classes
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
    
    def parse_meetings(self, meetings):
        meetings = meetings.split("\n")
        times = []
        location = ""
        for time in meetings:
            t, l = self.parse_meeting_times(time)
            # really bad way to do this but also workday formatted is retarded so I gotta match it
            location = l
            times.append(t)
        return times, location

    def parse_meeting_times(self, meeting_times: str):
        parts = meeting_times.split('|')
    
        times = '|'.join(parts[:3])
    
        location = '|'.join(parts[3:])
        return times, location

    def row_to_course_info(self, row_num: int) -> Course_Info:
        # important_cols = ["course listing", "section", "meeting patterns", "instructor"]
        dataframe = self.schedule_data
     
        data_row = dataframe.iloc[row_num]
        
        # ok i genuinely dont know why but I LITERALLY had the same thing but retyping it fixed it
        return Course_Info(
            name=data_row['course listing'],
            section=data_row['section'],
            instructor=data_row['instructor'],
            meeting_times=data_row['meeting patterns']
        )
    def get_courses(self) -> List[Course_Info]:
        all_courses = []
        for i in range(len(self.schedule_data)):
            all_courses.append(self.row_to_course_info(i))
        return all_courses




