import hashlib
import os

def authenticate_user(user_id, password):
    """Simulate user authentication by hashing password."""
    stored_hash = hashlib.sha256("password123".encode()).hexdigest()
    input_hash = hashlib.sha256(password.encode()).hexdigest()
    return input_hash == stored_hash
