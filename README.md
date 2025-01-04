# **Standardizing Univaffils Plan/Approach**
##### by Sophia 

## Pre-Face
This is a sample of the code I wrote during my time at the NBER. Some references and names are purposefully made to be obscure and generalized.

### Summary of What I Did:
There is a database of 100k people that all have manually/self-entered university affiliations, and the first part of this project was to clean up and standardize the affiliations for all of these people. The data was cleaned and standardized, then I wrote a custom SQL table API in order to modify, maintain, and upkeep the SQL table that contains the list of standardized affiliation names. 

## File Organization 

### Directories in Use
#### sql
This directory contains my sql table API for modifying the related tables in the NBER database to eventually be displayed on the website.

`canonical_table_functions.py` 
* This file contains functions that allow for the modification of the table that contains the canonical university affiliation values.                

`table_functions.py` 
* This file contains functions that allow for modification of the [table name] table (mostly the univaffil column) 

`sql_constants`
* Queries and constants used are stored here

`sql_utilities`
* Utility functions for sql queries such as **execute_sql** and connecting to the server

#### src
This is the folder with the main scripts needed to run.

**spreadsheets**  
In this folder, you want to import and push/pull the changes made to the spreadsheets Greta will edit in order for those changes to take effect when running the scripts   

`modify_table_from_file.py`
* a script that helps you modify the canonical_values table 
* any changes made to the canonical_values table should be done through or reflect the design of this script.
`replace_univaffil_from_file.py`
* a script that replaces universally a given non-standardized univaffil with a standardized univaffil. 

`affiliate_get_std_name_to_tsv.py`
* gets the scores of affiliates matched to the canonical_values table
* The tsv files underneath this section reflect the output of this script

`working_paper_author_get_std_name_to_tsv.py`
* gets the scores of working paper authors matched to the canonical_values table

### **Getting the Standardized Canonical List:**
Run the script `get_canonical_values.py` in \utils\verified_list 

## **Manual Work**
I have put in a shared drive all the intermediate spreadsheets that will be needed to manually update the affiliations.

## **Flow**
This is the ideal way for handling how to update the sql table after Greta finishes evaluating every University affiliations. 

### Step 1: Updating the Spreadsheets
Once all the spreadsheet work is done, export the `verified_affiliations` and `values_to_add` spreadsheets **as a tsv** and put them in either:
*  The gitlab affiliations project in /utils/verified_list/spreadsheets and push+pull the changes 
*  The file location of the project at /utils/verified_list/spreadsheets 

**This is a very important step** because functions to update the canonical_values table require these spreadsheets to both be a tsv AND in the right location. There will already be a placeholder file there, so that people do not get confused if they are in the right spot or not (just overwrite the already created file)

### Step 2: Updating the Canonical Values Table 
Once the spreadsheets are loaded, you want to run `modify_table_from_file.py` in src/spreadsheets and type '1' to add values into the canonical_values table from the file if new affiliations were discovered (likely will be).
This will update the canonical_values table and add all the affiliations that were missing before and manually added. This is important as without this step the new affiliations will NOT show up in the dropdown menu. 

### Step 3: Updating the [Table Name] Table
Once the standardized values for the tables are all imported as spreadsheets, all you need to do is run `replace_univaffil_from_file.py` in src/verified_list/spreadsheets.
And that is it!

## Maintaining the Canonical Values Table
I wrote a lot of functions in this project in the hopes that editing and changing the canonical values table will all go through functions in here. This is because there are a lot of checks in place which are necessary for making sure that the values in the univaffil column stay consistent with the values in the canonical_values table column.

It is imperative to run the `modify_table_from_file.py` file in src/verified_list/spreadsheet to add, delete, or replace any values in the canonical_values table to ensure everything goes smooth. 
OR you can write a custom script using functions from `canonical_values_table_functions.py` but make sure that **any** deletion, addition, or replacement in the canonical_values table is also reflected in the [Table Name] table as well!!

## Running the Matching Algorithm Again
If for any reason there comes the need to run the matching algorithm again, just run either `working_paper_author_get_std_name_to_tsv.py` and it will be output to working_paper_author_std_name_scores.tsv (or run the script for affiliates for a more narrow sample size). 

Copyright NBER and Sophia Yang 
