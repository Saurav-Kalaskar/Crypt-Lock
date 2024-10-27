import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def monitor_performance(start_time):
    """Log the time taken to process a request."""
    end_time = time.time()
    time_taken = end_time - start_time
    logger.info(f"Request processed in {time_taken:.2f} seconds.")
