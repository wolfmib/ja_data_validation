# data_total_test.py

import pandas as pd
from data_comple import check_data_completeness
from data_consis import check_data_consistency

def run_tests(data,data2):
    completeness_result, comple_info = check_data_completeness(data)
    validation_result , consis_info = check_data_consistency(data,data2)
    return completeness_result, validation_result , comple_info, consis_info

def print_summary(completeness_result, validation_result,i_comple_info, i_consis_info):
    print("=" * 33)
    print("|{:^13}|{:^13}|".format("test_category", "result"))
    print("-" * 33)
    print("|{:^13}|{:^13}|".format("completeness", completeness_result))
    print("-" * 33)
    print("|{:^13}|{:^13}|".format("validation", validation_result))
    print("=" * 33)


    ## Detail information
    print(f"For dataValidation completeness: \n {i_comple_info}")
    print(f"For dataValidation consistency:  \n {i_consis_info}")

# Example usage
if __name__ == "__main__":
    # Assume 'data' is a pandas DataFrame
    data = pd.DataFrame({'A': [1, 2, None, 4],
                         'B': ['x', 'y', 'z', None],
                         'C': [None, 'p', 'q', 'r']})
    
    data2 = pd.DataFrame({'A': [5, 6, 7, 8],
                      'D': ['a', 'b', 'c', 'd'],
                      'E': ['r', 's', 't', 'u']})




    #print out loding data
    print("False Case example")
    print(f"data1:\n{data.head(3)}\n...\n====================\n\n")
    print(f"data2:\n{data2.head(3)}\n...\n====================\n\n")

    completeness_result, consistency_result , comple_info, consis_info= run_tests(data,data2)  #Test
    print_summary(completeness_result, consistency_result,comple_info,consis_info) ##Summary





   
    ## True Case
    data = pd.DataFrame({'A': [1, 2, 4, 4],
                         'B': ['x', 'y', 'z', 'k'],
                         'C': ['q', 'p', 'q', 'r']})
    
    data2 = pd.DataFrame({'Z': [5, 6, 7, 8],
                      'D': ['a', 'b', 'c', 'd'],
                      'E': ['r', 's', 't', 'u']})




    #print out loding data
    print("Passed Case example")
    print(f"data1:\n{data.head(3)}\n...\n====================\n\n")
    print(f"data2:\n{data2.head(3)}\n...\n====================\n\n")

    completeness_result, consistency_result , comple_info, consis_info= run_tests(data,data2)  #Test
    print_summary(completeness_result, consistency_result,comple_info,consis_info) ##Summary


