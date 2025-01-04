import pandas as pd
import sys
sys.path.append('/path/to/project')

from sql.standardized_univaffils_table_functions import add_value_to_standardized_univaffil_table, remove_value_from_standardized_univaffil_table, \
    replace_value_in_standardized_univaffil_table
from src.verified_list.checks_before_modifying_canonical_values import get_type, check_univaffil_exists
from src.utils.helper_functions import get_user_yes_or_no

def add_values_from_file(filename="values_to_add.tsv", def_type=False):
    """
    Reads values from a file and adds them to the standardized university affiliations table.

    Args:
        filename (str): The name of the file containing values to add. Default is "values_to_add.tsv".
        def_type (bool): Whether to dynamically determine the value type. Default is False (uses 'affil').
    """
    df = pd.read_csv(filename, sep='\t')
    for value in df['value']:
        if def_type:
            value_type = get_type()
        else:
            value_type = 'affil'

        if check_univaffil_exists(value):
            print(f"{value} is already present in the database, ignoring this request.")
        else:
            add_value_to_standardized_univaffil_table(value_type, value, flags='')

def remove_values_from_file(filename="values_to_remove.tsv", def_type=False, check=False):
    """
    Reads values from a file and removes them from the standardized university affiliations table.

    Args:
        filename (str): The name of the file containing values to remove. Default is "values_to_remove.tsv".
        def_type (bool): Whether to dynamically determine the value type. Default is False (uses 'affil').
        check (bool): Whether to confirm removal if the value exists in the people table. Default is False.
    """
    df = pd.read_csv(filename, sep='\t')
    for value in df['value']:
        if def_type:
            value_type = get_type()
        else:
            value_type = 'affil'

        if check:
            if check_univaffil_exists(value):
                if get_user_yes_or_no("This value exists in the people table already, if you try to remove it, it will "
                                      "override the current value with an empty string, proceed?"):
                    remove_value_from_standardized_univaffil_table(value_type, value)
        else:
            remove_value_from_standardized_univaffil_table(value, value_type)

def replace_values_from_file(filename="values_to_replace.tsv"):
    """
    Reads values from a file and replaces them in the standardized university affiliations table.

    Args:
        filename (str): The name of the file containing values to replace. Default is "values_to_replace.tsv".
    """
    df = pd.read_csv(filename, sep='\t')
    print(df.columns)  # Print the column names to check if 'original' exists
    for index, row in df.iterrows():
        original = row['original']
        replacement = row['replacement']
        replace_value_in_standardized_univaffil_table(original, replacement)

def main():
    """
    Main menu for the script. Provides options to add, remove, or replace values in the standardized university affiliations table.
    """
    while True:
        print("\nChoose an option:")
        print("1. Add values from file")
        print("2. Remove values from file")
        print("3. Replace values from file")
        print("q. Exit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == '1':
            add_values_from_file()
        elif choice == '2':
            remove_values_from_file()
        elif choice == '3':
            replace_values_from_file()
        elif choice == 'q':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or q.")

if __name__ == "__main__":
    main()
