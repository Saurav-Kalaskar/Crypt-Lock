import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def trigger_security_alert(message):
    """Simulate sending a security alert."""
    logger.warning(f"Security Alert: {message}")
