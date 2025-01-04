import pymysql
import logging

from sql.sql_constants import MYSQL_HOST, MYSQL_DATABASE

def get_mysql_password():
    """
    Get the password to the mysql server
    """
    try:
        with open('path/to/mysql/server/password', 'r') as f:
            password = f.read().strip()
        return password
    except FileNotFoundError:
        raise Exception("Password file not found")
    except Exception as e:
        raise Exception(f"An error occurred while reading the password: {e}")


def connect_sql():
    """ Connect to SQL server and return the connection
    """
    try:
        conn = pymysql.connect(user="nobody", password=get_mysql_password(), host=MYSQL_HOST, database=MYSQL_DATABASE, charset='utf8mb4')
        logging.info("Connected successfully to MariaDB!")
    except pymysql.Error as e:
        logging.error(f"Error connecting to MariaDB: {e}")
        return f"executeSQL// SOMETHING WENT WRONG{e}"
    
    cur = conn.cursor(pymysql.cursors.DictCursor)
    return cur, conn


def execute_sql(qry, params=None):
    """ Connect to SQL server and execute a given query with optional parameters

    :param qry: query to be executed by MySQL
    :param params: parameters to be passed to the query (default is None)
    :returns: Results from query or success message
    """
    logging.info(f"Executing query: {qry}")
    cur, conn = connect_sql()
    results = {}

    try:
        if params:
            cur.execute(qry, params)  # use parameters if provided
        else:
            cur.execute(qry)  # execute without parameters if none provided

        conn.commit()  # ensure changes are committed to the database
        results = cur.fetchall()
        logging.info("Success executing query!!")
    except pymysql.Error as e:
        logging.error(f"Error executing query: {e}")
        return "SOMETHING WENT WRONG"
    finally:
        cur.close()
        conn.close()

    if results:
        return results

    return "SQL query executed successfully"



