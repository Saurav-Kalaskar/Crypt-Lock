import hashlib

def hash_password(password):
    """Hash a password for storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_password(password, hashed_password):
    """Validate a password by comparing its hash."""
    return hash_password(password) == hashed_password
