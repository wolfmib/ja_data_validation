def check_data_consistency(data1, data2):
    similar_columns = []
    for column1 in data1.columns:
        for column2 in data2.columns:
            if column1.lower() == column2.lower():
                similar_columns.append(column1)
                break  # Exit inner loop if a similar column is found
    if similar_columns:
        msg = "Data consistency check failed. Similar column names found when merging datasets:\n"
        for column in similar_columns:
            msg += f"- {column}\n"

        return False, msg
    else:
        msg = "Data consistency check passed. No similar column names found.\n"
        return True, msg

