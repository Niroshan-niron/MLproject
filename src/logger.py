import logging
import os
from datetime import datetime

# Correct log file format (slashes are invalid in filenames)
LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"

# Create "logs" directory if it doesn't exist
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


