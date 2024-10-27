import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DDoSProtection:
    """Simple rate-limiting for DDoS protection."""
    
    def __init__(self, max_requests_per_minute=10):
        self.max_requests = max_requests_per_minute
        self.request_counts = {}
        self.time_window = 60  # seconds

    def is_request_allowed(self, user_ip):
        current_time = time.time()
        
        if user_ip not in self.request_counts:
            self.request_counts[user_ip] = []
        
        # Clean up old requests
        self.request_counts[user_ip] = [
            timestamp for timestamp in self.request_counts[user_ip] if current_time - timestamp < self.time_window
        ]
        
        if len(self.request_counts[user_ip]) < self.max_requests:
            self.request_counts[user_ip].append(current_time)
            logger.info(f"Request allowed for IP: {user_ip}")
            return True
        else:
            logger.warning(f"DDoS protection triggered for IP: {user_ip}")
            return False
    
    def check_protection_status(self, user_ip):
        """Check and log whether the user is protected from DDoS."""
        if self.is_request_allowed(user_ip):
            logger.info(f"IP {user_ip} is currently protected under DDoS limits.")
            return "You are protected from DDoS attacks."
        else:
            logger.warning(f"IP {user_ip} exceeded DDoS limits and is blocked.")
            return "DDoS protection triggered. You are blocked from further requests for a while."
