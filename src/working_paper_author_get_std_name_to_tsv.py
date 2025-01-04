# import the file path
import sys
sys.path.append('/path/to/project')

import pandas as pd
from sql.sql_utilities import execute_sql
from sql.sql_constants import VERIFIED_AFFILS_QUERY, WORKING_PAPER_AUTHOR_QUERY
from src.utils.get_best_match import get_best_match

def get_min_score():
    """
    Prompts the user to input a minimum match score for RapidFuzz to use.

    Continuously requests user input until a valid score between 0 and 100 is entered.

    Returns:
        int: The valid minimum match score selected by the user.
    """
    while True:
        user_input = input("Choose your minimum match score for RapidFuzz to use (0-100): ")

        if user_input.isdigit():
            user_input = int(user_input)
            if 0 <= user_input <= 100:
                break
            else:
                print("Please enter a number between 0 and 100.")
        else:
            print("Invalid input! Please enter a valid number between 0 and 100.")

    return user_input

def output_to_tsv(affiliates):
    """
    Saves the given affiliate data to a CSV file.

    Args:
        affiliates (DataFrame): The affiliate data to save as a CSV file.

    Returns:
        None
    """
    affiliates.to_csv('working_paper_author_std_name_scores.tsv', sep='\t', index=False)


def main():
    # the data being queried is currently only the NBER affiliates
    affiliates = pd.DataFrame(execute_sql(WORKING_PAPER_AUTHOR_QUERY))
    verified_affiliates = execute_sql(VERIFIED_AFFILS_QUERY)
    verified_affiliates = [affiliate['value'] for affiliate in verified_affiliates]

    choice = get_min_score()

    # lambda that fills the standardized column and score column
    affiliates[['Standardized', 'Score']] = affiliates['univaffil'].apply(
        lambda x: pd.Series(get_best_match(x, verified_affiliates, choice))
    )

    # write output to csv file
    output_to_tsv(affiliates)


if __name__ == "__main__":
    main()