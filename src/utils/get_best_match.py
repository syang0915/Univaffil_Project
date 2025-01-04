from rapidfuzz import fuzz

import re

def preprocess(s):
    """
    Normalize the string by converting it to lowercase and removing non-alphanumeric characters.

    Args:
        s (str): The input string to preprocess.

    Returns:
        str: The preprocessed string with all letters in lowercase and non-alphanumeric characters removed.
    """
    s = s.lower()
    s = re.sub(r'\W+', ' ', s)
    return s

def rapidfuzz_metrics(affiliate, verified):
    """
    Compute similarity scores between two strings using RapidFuzz metrics.

    Args:
        affiliate (str): The first string (affiliate) to compare.
        verified (str): The second string (verified) to compare.

    Returns:
        list of tuples: A list containing tuples with the metric name and the corresponding similarity score.
                         Each tuple contains:
                            - ('token_sort_ratio', score)
    """
    return [
        ('token_sort_ratio', fuzz.token_sort_ratio(affiliate, verified)),
    ]

def get_best_match(affiliate, verified_list, min_score=80, clean=True):
    """
    Find the best match from a list of verified affiliates for a given affiliate string,
    based on a combination of RapidFuzz similarity and cosine similarity scores.

    Args:
        affiliate (str): The affiliate string to compare.
        verified_list (list of str): A list of verified affiliate strings to match against.
        min_score (int, optional): The minimum score threshold for considering a match. Defaults to 80.
        clean (bool, optional): If True, the affiliate string will be cleaned before matching.
    Returns:
        tuple: A tuple containing:
            - str: The best matching verified affiliate string (or empty string if no match is found above the threshold).
            - float: The best similarity score.
    """
    best_match = ''
    best_score = 0

    # preprocess the affiliate string
    affiliate_clean = affiliate.lower().strip()
    if clean:
        affiliate_clean = preprocess(affiliate)

    for verified in verified_list:
        # preprocess each string in the verified list
        verified_clean = preprocess(verified)

        # rapidfuzz
        for name, score in rapidfuzz_metrics(affiliate_clean, verified_clean):
            if score > best_score:
                best_match = verified
                best_score = score

    if best_score >= min_score:
        print(f"Match found!: {best_match}")
        return best_match, best_score
    else:
        print("No match!")
        return '', 0
