import logging
from datetime import datetime
import os

# Define log folder and ensure it exists
LOG_FOLDER = "AuditLogging/logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

def setup_logger(log_type):
    """
    Sets up a logger for a specific log type (access, password_change, or audit_trail).
    Log files are named based on the current date (e.g., access_20231025.log).
    """
    # Generate log file name based on type and date
    current_date = datetime.now().strftime("%Y%m%d")
    log_file = os.path.join(LOG_FOLDER, f"{log_type}_{current_date}.log")

    # Configure logger
    logger = logging.getLogger(log_type)
    logger.setLevel(logging.INFO)

    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(file_handler)

    return logger

# Loggers for different types of events
access_logger = setup_logger("access")
password_change_logger = setup_logger("password_change")
audit_trail_logger = setup_logger("audit_trail")

def log_access_attempt(user_id, success):
    """
    Logs an access attempt.
    """
    status = "SUCCESS" if success else "FAILURE"
    access_logger.info(f"User {user_id} attempted access. Status: {status}")

def log_password_change(user_id, old_hash, new_hash):
    """
    Logs a password change event.
    """
    password_change_logger.info(
        f"User {user_id} changed password. Old hash: {old_hash}, New hash: {new_hash}"
    )

def log_audit_event(event_type, message):
    """
    Logs a general audit event.
    """
    audit_trail_logger.info(f"{event_type}: {message}")