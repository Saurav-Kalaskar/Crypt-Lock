import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def track_delivery(order_id, status):
    """Simulate delivery tracking."""
    logger.info(f"Order {order_id}: Delivery status updated to {status}.")
