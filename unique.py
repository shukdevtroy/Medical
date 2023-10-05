import pandas as pd

# Load the CSV file into a pandas DataFrame
csv_file_path = 'DiseaseDept2.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Specify the column for which you want to find unique values
column_name = 'Department'  # Replace with the name of your target column

# Use the unique() function to find unique values in the specified column
unique_values = df[column_name].unique()

# Print the unique values
print("Unique values in the column '{}':".format(column_name))
for value in unique_values:
    print(value)

# Use the nunique() function to count unique values in the specified column
unique_values_count = df[column_name].nunique()

print(f'Number of unique values in column "{column_name}": {unique_values_count}')