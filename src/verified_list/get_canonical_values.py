# gets the canonical values table
import pandas as pd
import sys

sys.path.append('/path/to/project')

from sql.sql_constants import VERIFIED_AFFILS_QUERY
from sql.sql_utilities import execute_sql

df = pd.DataFrame(execute_sql(VERIFIED_AFFILS_QUERY))
df.to_csv("/spreadsheets/canonical_values_table.tsv", sep='\t', index=False)