import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def detect_fraud(transaction_data):
    """Simulate fraud detection on a transaction."""
    # Placeholder logic for fraud detection
    is_fraudulent = transaction_data.get('amount', 0) > 10000  # Example rule: high transaction amount
    if is_fraudulent:
        logger.warning(f"Fraud detected in transaction: {transaction_data}")
    else:
        logger.info("Transaction passed fraud detection.")
    return is_fraudulent
