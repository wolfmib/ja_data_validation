def check_data_consistency(data1, data2):
    similar_columns = []
    for column1 in data1.columns:
        for column2 in data2.columns:
            if column1.lower() == column2.lower():
                similar_columns.append(column1)
                break  # Exit inner loop if a similar column is found
    if similar_columns:
        print("Data consistency check failed. Similar column names found when merging datasets:")
        for column in similar_columns:
            print(f"- {column}")
    else:
        print("Data consistency check passed. No similar column names found.")

# Example usage
import pandas as pd

# Assume 'data1' and 'data2' are pandas DataFrames
data1 = pd.DataFrame({'A': [1, 2, 3, 4],
                      'B': ['x', 'y', 'x', 'y'],
                      'C': ['p', 'p', 'q', 'q']})

data2 = pd.DataFrame({'A': [5, 6, 7, 8],
                      'D': ['a', 'b', 'c', 'd'],
                      'E': ['r', 's', 't', 'u']})

check_data_consistency(data1, data2)

