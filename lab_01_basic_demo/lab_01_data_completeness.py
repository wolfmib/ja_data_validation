def check_data_completeness(data):
    missing_values = []
    for column in data.columns:
        if data[column].isnull().any():
            missing_values.append(column)
    if missing_values:
        print("Data completeness check failed. Missing values found in columns:")
        for column in missing_values:
            print(f"- {column}")
    else:
        print("Data completeness check passed. No missing values found.")

# Example usage
import pandas as pd

# Assume 'data' is a pandas DataFrame
data = pd.DataFrame({'A': [1, 2, 7, 4],  # passed column
                     'B': ['x', 'y', 'z', None], # missing col.
                     'C': [None, 'p', 'q', 'r']}) #missing col.


print(f"Total columns: {data.columns}")
print("------- missing columns ------")
check_data_completeness(data)

