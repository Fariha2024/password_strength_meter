import os
import glob
from datetime import datetime, timedelta

def rotate_logs(log_folder, days_to_keep=30):
    """Deletes log files older than `days_to_keep`."""
    cutoff = datetime.now() - timedelta(days=days_to_keep)
    for log_file in glob.glob(os.path.join(log_folder, "*.log")):
        file_creation_time = datetime.fromtimestamp(os.path.getctime(log_file))
        if file_creation_time < cutoff:
            os.remove(log_file)
            print(f"Deleted old log file: {log_file}")