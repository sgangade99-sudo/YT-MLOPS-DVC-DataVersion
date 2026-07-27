import pandas as pd
import os

# create a sample DataFrame with column name 
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25,30,35],
        'City': ['NewYork', 'Los Angles', 'Chicago']}

df = pd.DataFrame(data)

# adding a new row to df for V2

# new_row_loc =  {'Name': 'V2', 'Age': 20, 'City': 'City1'}
# df.loc[len(df.index)] = new_row_loc

# # adding new row to df for V3

# new_row_loc2 = {'Name': 'V3', 'Age': 30, 'City': 'City1'}
# df.loc[len(df.index)] = new_row_loc2

# ensure the "data" directory exist at root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# save the DataFrame to a csv file including column name 
df.to_csv(file_path, index = False)

print(f'CSV file saved to {file_path}')