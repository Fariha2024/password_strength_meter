def assign_score(analysis):
    """
    Assign a score to the password based on the analysis results.
    
    Args:
        analysis (dict): The results of the password analysis.
    
    Returns:
        int: A score between 1 and 4.
    """
    score = 0
    if analysis["length_valid"]:
        score += 1
    if analysis["case_valid"]:
        score += 1
    if analysis["digits_symbols_valid"]:
        score += 1
    if analysis["not_blacklisted"]:
        score += 1
    return score