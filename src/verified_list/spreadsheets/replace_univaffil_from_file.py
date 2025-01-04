import sys
sys.path.append('/path/to/project')

import pandas as pd
from sql.table_functions import update_affiliates_in_people_table_from_df

df = pd.read_csv('verified_affiliations.tsv', sep='\t')
update_affiliates_in_people_table_from_df(df)