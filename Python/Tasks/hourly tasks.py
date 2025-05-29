import logging
import datetime
import os
import time # For the example placeholder task

# --- Configuration ---
# Get the directory where the script is located to ensure logs are written there
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(SCRIPT_DIR, 'hourly_task.log')

# --- Logging Setup ---
# Configure logging to write to a file and also to the console (for debugging when run manually)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=LOG_FILE,
    filemode='a' # Append to the log file
)
# Also add a console handler so you see output when running manually
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(console_handler)

def perform_my_hourly_task():
    """
    This function contains the actual task you want to run every hour.
    Replace this with your own Python code.
    """
    logging.info("Starting hourly task...")
    
    # --- YOUR CUSTOM HOURLY CODE GOES HERE ---
    # Example: Print some system info, process data, check a service, etc.
    try:
        # Simulate some work
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Hourly task executed at: {current_time}")
        logging.info("Example: Checked for new data, processed files, etc.")
        # Example of a simple file operation
        with open(os.path.join(SCRIPT_DIR, 'task_marker.txt'), 'a') as f:
            f.write(f"Task ran at {current_time}\n")

    except Exception as e:
        logging.error(f"An error occurred during the hourly task: {e}")
    # --- END OF YOUR CUSTOM HOURLY CODE ---

    logging.info("Hourly task finished.")

if __name__ == "__main__":
    logging.info("Script started by scheduler or manually.")
    perform_my_hourly_task()
    logging.info("Script completed.")
