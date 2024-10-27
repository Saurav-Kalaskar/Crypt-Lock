import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_customer_behavior(action, details):
    """Log customer behavior for analysis."""
    logger.info(f"Customer action logged: {action} - Details: {details}")
