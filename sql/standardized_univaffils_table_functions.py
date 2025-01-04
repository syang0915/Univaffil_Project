import pandas as pd
import sys

sys.path.append('/path/to/project')

from src.utils.get_best_match import get_best_match
from sql.sql_constants import DELETE_FROM_SQL_TABLE_QUERY_2_VALUE_TYPE, \
    ADD_ENTRY_TO_STANDARDIZED_UNIVAFFIL_TABLE_3_TYPE_VALUE_FLAGS, \
    VERIFIED_AFFILS_QUERY, REPLACE_IN_STANDARDIZED_UNIVAFFIL_TABLE_QUERY_2_NEW_ORIGINAL, \
    CHECK_ENTRY_EXISTS_IN_STANDARDIZED_UNIVAFFIL_TABLE_1_VALUE, UNIVERSAL_REPLACE_QUERY_ON_AFFILIATE_TABLE_NAME_2_NEW_ORIGINAL
from sql.sql_utilities import execute_sql

def add_value_to_standardized_univaffil_table(value_type, value, flags):
    """
    Adds a verified affiliation to the canonical_values table in the SQL server.

    Parameters:
        value_type (str): The type of affiliation being added to the SQL table.
                          Possible values: 'affil', 'school', 'confloc'.
        value (str): The affiliate name to be added to the SQL table.
        flags (str): The flags of the affiliation (if any), which may represent additional metadata.

    Returns:
        None: This function does not return any value. It performs an SQL query to add the entry.
    """
    execute_sql(ADD_ENTRY_TO_STANDARDIZED_UNIVAFFIL_TABLE_3_TYPE_VALUE_FLAGS, params=[value_type, value, flags])


def remove_value_from_standardized_univaffil_table(value, value_type):
    """
    Removes an affiliation entry from the canonical_values table in the SQL server.

    Parameters:
        value (str): The affiliate name to be removed from the SQL table.
        value_type (str): The type of affiliation to be removed from the SQL table.
                          Possible values: 'affil', 'school', 'confloc'.

    Returns:
        None: This function does not return any value. It performs an SQL query to remove the entry.
    """
    execute_sql(DELETE_FROM_SQL_TABLE_QUERY_2_VALUE_TYPE, params=[value, value_type])


def replace_value_in_standardized_univaffil_table(value, replacement, replace_people_too=True):
    """
    Replaces an existing affiliation entry with a new one in the canonical_values table.

    Parameters:
        value (str): The current affiliation value to be replaced.
        replacement (str): The new value that will replace the existing affiliation.
        replace_people_too (bool, optional): If True, replaces the value in the people table as well.
                                             Defaults to True.

    Returns:
        None: This function does not return any value. It performs an SQL query to update the entries.
    """
    execute_sql(REPLACE_IN_STANDARDIZED_UNIVAFFIL_TABLE_QUERY_2_NEW_ORIGINAL, params=[replacement, value])
    if replace_people_too:
        execute_sql(UNIVERSAL_REPLACE_QUERY_ON_AFFILIATE_TABLE_NAME_2_NEW_ORIGINAL, params=[replacement, value])


def check_similar_entries(value):
    """
    Checks for similar entries in the canonical_values table using a similarity score.

    Parameters:
        value (str): The affiliation value to check for similarity.

    Returns:
        tuple: A tuple containing:
            - best_match (str): The closest matching entry from the table.
            - best_score (float): The similarity score of the best match.
    """
    df = pd.DataFrame(execute_sql(VERIFIED_AFFILS_QUERY))
    best_match, best_score = get_best_match(value, df['value'], clean=False)
    return best_match, best_score


def check_value_exists_in_standardized_univaffil_table(value):
    """
    Checks if a specific affiliation value exists in the canonical_values table.

    Parameters:
        value (str): The affiliation value to check for existence.

    Returns:
        bool: True if the value exists in the canonical_values table, otherwise False.
    """
    result = execute_sql(CHECK_ENTRY_EXISTS_IN_STANDARDIZED_UNIVAFFIL_TABLE_1_VALUE, params=[value])
    if result[0]['entry_exists']:
        print(f"executesql returned {result[0]}\nfull: {result}")
        return True
    else:
        print(f"executesql returned {result[0]}\nfull: {result}")
        return False

