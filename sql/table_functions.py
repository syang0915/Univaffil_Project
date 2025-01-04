import sys
sys.path.append('/path/to/project')

from sql_constants import UNIVERSAL_REPLACE_QUERY_ON_AFFILIATE_TABLE_NAME_2_NEW_ORIGINAL, CHECK_UNIVAFFIL_EXISTS_IN_TABLE_NAME_1_VALUE
from sql_utilities import execute_sql

def update_affiliates_in_people_table_from_df(affiliates):
    """
    update the entries in the sql query with the standardized affiliate name.

    affiliates: the df of affiliates that need replacing
    """
    for index, row in affiliates.iterrows():
        original_name = row['univaffil']
        standardized_name = row['univaffil_std']

        if standardized_name:
            sql_query = UNIVERSAL_REPLACE_QUERY_ON_AFFILIATE_TABLE_NAME_2_NEW_ORIGINAL
            params = (standardized_name, original_name)
            execute_sql(sql_query, params)

def check_univaffil_exists_in_people_table(value):
    """
    Checks if a university affiliation already exists in the people table
    """
    return execute_sql(CHECK_UNIVAFFIL_EXISTS_IN_TABLE_NAME_1_VALUE, value)