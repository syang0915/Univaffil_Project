MYSQL_HOST = 'host_server_name'
MYSQL_DATABASE = 'database_name'

univaffil_column_name_ENUM_TYPES = ['types']

# Queries that get data
GET_DISTINCT_UNIVAFFILS_QUERY = ("SELECT DISTINCT univaffil_column_name FROM affiliate_table_name WHERE univaffil_column_name IS NOT NULL AND univaffil_column_name != '' AND "
                             "(affiliate_identifier_flag != '' OR affiliate_identifier_flag IS NOT NULL)")
GET_ALL_UNIVAFFILS_QUERY = ("SELECT univaffil_column_name FROM affiliate_table_name WHERE univaffil_column_name IS NOT NULL AND univaffil_column_name != '' AND (affiliate_identifier_flag != "
                        "'' OR affiliate_identifier_flag IS NOT NULL)")
ALL_AUTHORS_QUERY = ("SELECT univaffil_column_name FROM affiliate_table_name WHERE univaffil_column_name IS NOT NULL AND univaffil_column_name != '' AND (affiliate_identifier_flag = '' "
                     "OR affiliate_identifier_flag IS NULL)")
CURR_AFFILIATES_QUERY = ("SELECT DISTINCT univaffil_column_name FROM affiliate_table_name WHERE univaffil_column_name IS NOT NULL AND univaffil_column_name != '' AND "
                         "affiliate_identifier_flag != ''")
VERIFIED_AFFILS_QUERY = ("SELECT DISTINCT value FROM standardized_univaffil_table_name"
                         " WHERE type = 'affil'")
CHECK_ENTRY_EXISTS_IN_STANDARDIZED_UNIVAFFIL_TABLE_1_VALUE = ("SELECT EXISTS(SELECT 1 FROM standardized_univaffil_table_name"
                                                              " WHERE value = %s) "
                                          "AS entry_exists")
CHECK_UNIVAFFIL_EXISTS_IN_TABLE_NAME_1_VALUE = ("SELECT EXISTS(SELECT 1 FROM affiliate_table_name WHERE univaffil_column_name = %s) "
                                          "AS entry_exists")
WORKING_PAPER_AUTHOR_QUERY = ("SELECT DISTINCT univaffil_column_name FROM affiliate_table_name WHERE univaffil_column_name IS NOT NULL AND univaffil_column_name != '' AND "
                              "user IN (SELECT DISTINCT author_user FROM working_papers_authors WHERE paper LIKE 'W%')")

# Queries that modify table
UNIVERSAL_REPLACE_QUERY_ON_AFFILIATE_TABLE_NAME_2_NEW_ORIGINAL = "UPDATE affiliate_table_name SET univaffil_column_name = %s WHERE univaffil_column_name = %s"
ADD_ENTRY_TO_STANDARDIZED_UNIVAFFIL_TABLE_3_TYPE_VALUE_FLAGS = ("INSERT INTO standardized_univaffil_table_name"
                                                                " (type, value, flags) VALUES (%s, %s, %s)")
DELETE_FROM_SQL_TABLE_QUERY_2_VALUE_TYPE = ("DELETE FROM standardized_univaffil_table_name"
                                            " WHERE value = %s AND type = %s")
REPLACE_IN_STANDARDIZED_UNIVAFFIL_TABLE_QUERY_2_NEW_ORIGINAL = ("UPDATE standardized_univaffil_table_name"
                                                                " SET value = %s WHERE value = %s")

