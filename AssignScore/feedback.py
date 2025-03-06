def get_feedback(score):
    """
    Provide feedback based on the password score.
    
    Args:
        score (int): The password score (1-4).
    
    Returns:
        tuple: A tuple containing the strength level and feedback message.
    """
    if score <= 2:
        return "Weak", "Your password is too short or missing key elements. Add at least 8 characters, including uppercase letters, digits, and symbols."
    elif score == 3:
        return "Moderate", "Your password is good but could be stronger. Add a special character (!@#$%^&*)."
    else:
        return "Strong", "Your password is strong and meets all security criteria."
    