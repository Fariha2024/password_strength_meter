from .check_length import check_length
from .check_case import check_case
from .check_digits_symbols import check_digits_symbols
from .blacklist_common_passwords import is_password_blacklisted
from AssignScore.assign_score import assign_score
from AssignScore.feedback import get_feedback

def analyze_password(password):
    """
    Analyze the password based on length, case, digits/symbols, and blacklist.
    
    Args:
        password (str): The password to analyze.
    
    Returns:
        dict: A dictionary containing the results of each check, score, and feedback.
    """
    length_valid = check_length(password)
    case_valid = check_case(password)
    digits_symbols_valid = check_digits_symbols(password)
    not_blacklisted = is_password_blacklisted(password)

    # Assign score and get feedback
    score = assign_score({
        "length_valid": length_valid,
        "case_valid": case_valid,
        "digits_symbols_valid": digits_symbols_valid,
        "not_blacklisted": not_blacklisted,
    })
    strength, feedback = get_feedback(score)

    return {
        "length_valid": length_valid,
        "case_valid": case_valid,
        "digits_symbols_valid": digits_symbols_valid,
        "not_blacklisted": not_blacklisted,
        "score": score,
        "strength": strength,
        "feedback": feedback,
    }