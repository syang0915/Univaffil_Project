from sql.standardized_univaffils_table_functions import check_value_exists_in_standardized_univaffil_table
from sql.sql_constants import univaffil_column_name_ENUM_TYPES

def get_type():
    ans = ''
    while ans not in univaffil_column_name_ENUM_TYPES:
        ans = input(f"Please enter what the type of this univaffil is: {univaffil_column_name_ENUM_TYPES}")
    return ans

def check_univaffil_exists(value):
    if check_value_exists_in_standardized_univaffil_table(value):
        print("This exact value currently exists in the standardized univaffil column."
              "\nPlease make sure you remove it before trying to modify or change it")
        return True
    else: return False