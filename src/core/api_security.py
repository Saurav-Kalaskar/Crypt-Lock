import logging
import os
from functools import wraps
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Retrieve the secure API key from environment variables
SECURE_API_KEY = os.getenv("SECURE_API_KEY")

def api_key_required(f):
    """Decorator to enforce API key authentication."""
    @wraps(f)
    def decorated_function(api_key, *args, **kwargs):
        if api_key != SECURE_API_KEY:  # Checks against the secure key from environment
            logger.warning("Unauthorized API access attempt.")
            return {"error": "Unauthorized"}, 403
        logger.info("API access authorized.")
        return f(*args, **kwargs)
    return decorated_function

# Example usage
@api_key_required
def get_secure_data(api_key):
    return {"data": "Sensitive information"}
