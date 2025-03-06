import streamlit as st

def display_strength_meter(score):
    """
    Display a visual strength meter based on the password score.
    
    Args:
        score (int): The password score (1-4).
    """
    if score <= 2:
        st.progress(score / 4)
        st.error("Weak Password")
    elif score == 3:
        st.progress(score / 4)
        st.warning("Moderate Password")
    else:
        st.progress(score / 4)
        st.success("Strong Password")
        