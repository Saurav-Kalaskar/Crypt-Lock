from cryptography.fernet import Fernet
import os

# Generate or load encryption key (for demo purposes, a static key)
ENCRYPTION_KEY = Fernet.generate_key()
cipher = Fernet(ENCRYPTION_KEY)

def encrypt_data(data):
    """Encrypt data."""
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data.decode()
