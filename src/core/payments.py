import re
from datetime import datetime

def validate_card_number(card_number):
    """Validates the card number using the Luhn algorithm."""
    def luhn_algorithm(n):
        r = [int(ch) for ch in str(n)][::-1]
        return sum(r[0::2]) + sum([sum(divmod(d * 2, 10)) for d in r[1::2]]) % 10 == 0

    # Check if card number is 16 digits and passes Luhn algorithm
    return bool(re.fullmatch(r"\d{16}", card_number)) and luhn_algorithm(card_number)

def validate_cvv(cvv):
    """Validates that the CVV is a 3-digit code."""
    return bool(re.fullmatch(r"\d{3}", cvv))

def validate_expiry_date(expiry_date):
    """Validates expiry date format (MM/YY) and checks if it’s in the future."""
    if not re.fullmatch(r"(0[1-9]|1[0-2])/[0-9]{2}", expiry_date):
        return False
    # Convert expiry date to a datetime object for comparison
    exp_month, exp_year = map(int, expiry_date.split("/"))
    exp_year += 2000  # Adjust for 2-digit year format (YY)
    current_date = datetime.now()
    return datetime(exp_year, exp_month, 1) > current_date

def validate_amount(amount):
    """Checks if the amount is within a secure range (e.g., $1 - $10,000)."""
    return 1 <= amount <= 10000

def process_payment(amount, card_number, expiry_date, cvv):
    """Processes payment with security validations according to FDR norms."""
    if not validate_card_number(card_number):
        return "Invalid card number. Payment rejected for security reasons."

    if not validate_cvv(cvv):
        return "Invalid CVV. Payment rejected for security reasons."

    if not validate_expiry_date(expiry_date):
        return "Invalid expiry date. Payment rejected for security reasons."

    if not validate_amount(amount):
        return "Transaction amount not within acceptable limits."

    # All checks passed, consider payment secure
    return "Payment successful and secure"
