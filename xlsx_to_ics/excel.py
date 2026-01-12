import pandas as pd
import numpy as np
import warnings
# Filter out the specific openpyxl UserWarning
warnings.filterwarnings("ignore", category=UserWarning, module='openpyxl')

first_col_name: str = "start"
cols_to_drop = [first_col_name, "drop", "swap", "credits", "grading basis", "instructional format", "delivery mode"]

df: pd.DataFrame = pd.read_excel("View_My_Courses.xlsx", skiprows=2)
df.columns = df.columns.str.lower()
df.columns.values[0] = first_col_name



print(df.columns.values)
for col_name in cols_to_drop:
    try:
        df = df.drop(col_name, axis=1)
    except KeyError:
        print(col_name, "does not exist, skipping")


# df["section"] = df["section"].split(" ")[1]
df["section"] = df["section"].apply(lambda s: s.split(" ")[1])

print(df.columns.values)

print(df.head())

df_filtered = df[df['registration status'] == 'Registered']

def get_list_of_row(row_num, dataframe) -> list:
    list = []
    data_row = dataframe.iloc[row_num]
    print("-------print col info--------")
    for name, datapoint in data_row.items():
        print(f"{name} :  {datapoint}")
        if (datapoint is np.nan):
            # print("is nan omg")
            list.append("n/a")
        else:
            list.append(datapoint)
    return list

print(get_list_of_row(4, df))

