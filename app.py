import os
import streamlit as st
from AnalyzePassword.analyze_password import analyze_password
from SuggestPassword.customize_password import customize_password
from SecureStorage.hash_password import hash_password
from SecureStorage.store_password import store_password_db, store_password_file
from DisplayUI.strength_meter import display_strength_meter
from DisplayUI.interactive_feedback import provide_feedback
from AuditLogging.audit_logger import log_access_attempt, log_password_change
from AuditLogging.audit_logger import log_access_attempt, log_password_change, log_audit_event


st.title("🔐 Password Strength Meter")

# Password Input and Analysis
password = st.text_input("Enter your password:", type="password", key="password_input")

if password:
    analysis = analyze_password(password)
    score = analysis["score"]

    # Display Strength Meter
    st.write("### Password Strength Meter")
    display_strength_meter(score)

    # Display Analysis Results
    st.write("### Analysis Results:")
    st.write(f"**Length Valid:** {analysis['length_valid']}")
    st.write(f"**Case Valid:** {analysis['case_valid']}")
    st.write(f"**Digits & Symbols Valid:** {analysis['digits_symbols_valid']}")
    st.write(f"**Not Blacklisted:** {analysis['not_blacklisted']}")
    st.write(f"### Password Score: {score}/4")
    st.write(f"**Strength:** {analysis['strength']}")

    # Provide Interactive Feedback
    st.write("### Feedback:")
    feedback = provide_feedback(analysis)
    st.write(feedback)

    # Secure Password Storage
    if st.checkbox("Store Password Securely"):
        hashed_password = hash_password(password)
        st.write(f"**Hashed Password:** {hashed_password}")

        storage_option = st.radio("Choose storage option:", ("Database", "Local File"))
        if storage_option == "Database":
            store_password_db(hashed_password)
            st.success("Password stored securely in the database!")
        else:
            store_password_file(hashed_password)
            st.success("Password stored securely in a local file!")

# Password Generator
st.write("### Generate a Strong Password")
length = st.slider("Select password length:", min_value=8, max_value=20, value=12)
include_symbols = st.checkbox("Include symbols (!@#$%^&*)", value=True)

if st.button("Generate Password"):
    strong_password = customize_password(length, include_symbols)
    st.write(f"**Generated Password:** {strong_password}")



    
# Log access attempt
log_access_attempt(user_id="user123", success=True)

# Log password change
log_password_change(user_id="user123", old_hash="hash1", new_hash="hash2")



# Streamlit app title
st.title("Audit Logging Example")

# Log an access attempt
if st.button("Log Access Attempt"):
    log_access_attempt(user_id="user123", success=True)
    st.success("Logged access attempt!")

# Log a password change
if st.button("Log Password Change"):
    log_password_change(user_id="user123", old_hash="hash1", new_hash="hash2")
    st.success("Logged password change!")

# Log a general audit event
if st.button("Log Audit Event"):
    log_audit_event("CONFIG_CHANGE", "User updated system configuration")
    st.success("Logged audit event!")




    


# Add a title
st.title("🔒 PasswordStrengthMeter Project Guide")
st.markdown("Welcome to the **PasswordStrengthMeter** project! This guide provides an overview of the project structure, features, and usage.")


# Add a divider
st.divider()

# Section 1: Project Overview
st.header("📖 Project Overview")
st.markdown("""
**PasswordStrengthMeter** is a Python-based application designed to:
- Analyze password strength: Checks length, case sensitivity, digits, symbols, and common passwords.
- Score Assignment: Assign a score and provide feedback.
- Password Suggestions: Generates strong and customizable passwords.
- Secure Storage: Hashes and stores passwords securely.
- Audit Logging: Logs access attempts, password changes, and general audit trails, Log security events for auditing purposes
        

""")

# Section 2: Project Structure
st.header("📂 Project Structure")
st.markdown("Here’s the detailed structure of the project:")

# Display the project structure as a code block
project_structure = """
PasswordStrengthMeter/
├── AnalyzePassword/                  # Section 1: Password Analysis
│   ├── __init__.py                   # Makes the folder a Python package
│   ├── check_length.py               # Checks if the password meets minimum length requirements
│   ├── check_case.py                 # Checks for uppercase and lowercase letters
│   ├── check_digits_symbols.py       # Checks for digits and special symbols
│   ├── blacklist_common_passwords.py # Checks if the password is in a common passwords blacklist
│   ├── analyze_password.py           # Main script to analyze password strength
├── AssignScore/                      # Section 2: Assigning Scores and Feedback
│   ├── __init__.py                   # Makes the folder a Python package
│   ├── assign_score.py               # Assigns a score based on password analysis
│   ├── feedback.py                   # Provides feedback to the user based on the score
├── SuggestPassword/                  # Section 3: Password Suggestions
│   ├── __init__.py                   # Makes the folder a Python package
│   ├── generate_password.py          # Generates strong, random passwords
│   ├── customize_password.py         # Allows users to customize generated passwords
├── SecureStorage/                    # Section 4: Secure Password Storage
│   ├── __init__.py                   # Makes the folder a Python package
│   ├── hash_password.py              # Hashes passwords for secure storage
│   ├── store_password.py             # Stores hashed passwords securely
├── DisplayUI/                        # Section 5: User Interface
│   ├── __init__.py                   # Makes the folder a Python package
│   ├── strength_meter.py             # Displays a visual strength meter for passwords
│   ├── interactive_feedback.py       # Provides interactive feedback to users
├── AuditLogging/                     # Section 6: Audit and Logging
│   ├── __init__.py                   # Makes the folder a Python package
│   ├── audit_logger.py               # Logs security events (e.g., access attempts, password changes)
│   ├── log_rotation.py               # Manages log rotation and cleanup
│   ├── audit_config.yaml             # Configuration for logging (e.g., log levels, formats)
│   └── logs/                         # Folder to store log files
│       ├── access_logs/              # Logs for access attempts
│       │   └── access_YYYYMMDD.log   # Example: access_20231025.log
│       ├── password_change_logs/     # Logs for password changes
│       │   └── password_change_YYYYMMDD.log  # Example: password_change_20231025.log
│       └── audit_trail.log           # Consolidated audit trail log
├── app.py                            # Main Streamlit application file
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
"""
st.code(project_structure, language="plaintext")

# Section 3: Flowchart
st.header("📊 Flowchart")
st.markdown("Here’s the workflow of the project:")
import os
import streamlit as st

# Corrected file path (no extra quotes)
Visual = r"C:\Users\muham\Documents\passwordstrengthmeter\image\visual_4b7c3f5e-c3f9-4c03-a62a-2e7b6e457359.jpg"  # Removed space in filename

# Check if file exists before displaying
if os.path.exists(Visual):
    st.image(Visual, caption="Password Strength Meter Workflow", use_column_width=True)
else:
    st.error("⚠️ Image file not found. Please check the file path.")

# Section 4: Screenshots
st.header("📸 Screenshots")
st.markdown("Here are some screenshots of the app in action:")
import streamlit as st

# Use raw strings or double backslashes
screenshot_1 = r"C:\Users\muham\Documents\passwordstrengthmeter\image\whatsApp_image2025-03-06at14.08.49_f1bd9fb2.jpg"
screenshot_2 = r"C:\Users\muham\Documents\passwordstrengthmeter\image\flow_chart_717aa7c8-2b90-48d2-ba6d-bf00bcfe17b2.jpg"  # Renamed file

# Check if files exist before displaying
if os.path.exists(screenshot_1) and os.path.exists(screenshot_2):
    st.image([screenshot_1, screenshot_2], caption=["Screenshot 1", "Screenshot 2"], width=400)
else:
    st.error("⚠️ One or both image files were not found. Please check the file paths.")

# Section 5: Contributing
st.header("🤝 Contributing")
st.markdown("""
We welcome contributions! Here’s how you can contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.
""")

# Section 6: License
st.header("📜 License")
st.markdown("""
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
""")

# Add a footer
st.divider()
st.markdown("© 2023 PasswordStrengthMeter. All rights reserved.")