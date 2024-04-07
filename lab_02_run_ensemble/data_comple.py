# data_comple.py

def check_data_completeness(data):
    missing_values = []
    for column in data.columns:
        if data[column].isnull().any():
            missing_values.append(column)
    if missing_values:
        msg = "Data completeness check failed. Missing values found in columns:\n"
        for column in missing_values:
            msg += f"- {column}\n"

        return False, msg
    else:
        msg = "Data completeness check passed. No missing values found.\n"
        return True, msg

