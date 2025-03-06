def provide_feedback(analysis):
    """
    Provide real-time feedback based on the password analysis.
    
    Args:
        analysis (dict): The results of the password analysis.
    
    Returns:
        str: Feedback message.
    """
    feedback = []
    if not analysis["length_valid"]:
        feedback.append("Your password is too short. Add at least 8 characters.")
    if not analysis["case_valid"]:
        feedback.append("Your password should include both uppercase and lowercase letters.")
    if not analysis["digits_symbols_valid"]:
        feedback.append("Your password should include at least one digit and one special character.")
    if not analysis["not_blacklisted"]:
        feedback.append("Your password is too common. Choose a more unique password.")

    if not feedback:
        return "Your password is strong and meets all security criteria."
    return " ".join(feedback)