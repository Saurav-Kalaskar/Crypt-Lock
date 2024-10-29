import os
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
from src.core.encryption import encrypt_data
from src.core.auth import authenticate_user
from src.core.payments import process_payment
from src.core.fraud_detection import detect_fraud
from src.core.ddos_protection import DDoSProtection
from src.core.api_security import api_key_required
from src.monitoring.logger import log_event
from src.monitoring.metrics import get_real_time_metrics
from src.monitoring.data_integrity import check_data_integrity

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# DDoS protection instance
ddos_protection = DDoSProtection(max_requests_per_minute=10)

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    log_event("Health check requested.")
    return jsonify({"status": "OK", "message": "Server is running"}), 200

# Render home UI
@app.route('/')
def index():
    return render_template('index.html')

# Encryption endpoint
@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json().get("data")
    if not data:
        log_event("Encryption failed: No data provided.")
        return jsonify({"error": "No data provided"}), 400

    try:
        encrypted_data = encrypt_data(data)
        log_event("Data encrypted successfully.")
        return jsonify({"encrypted_data": encrypted_data})
    except Exception as e:
        log_event(f"Encryption error: {str(e)}")
        return jsonify({"error": "Encryption failed"}), 500

# Authentication endpoint
@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    user_id = data.get("user_id")
    password = data.get("password")
    
    if not user_id or not password:
        log_event("Authentication failed: Missing credentials.")
        return jsonify({"authenticated": False, "error": "Missing credentials"}), 400

    auth_status = authenticate_user(user_id, password)
    log_event("User authentication attempted.")
    return jsonify({"authenticated": auth_status})

# Payment processing endpoint
@app.route('/payment', methods=['POST'])
def payment():
    data = request.get_json()
    required_fields = ["amount", "card_number", "expiry_date", "cvv"]

    if not all(field in data for field in required_fields):
        log_event("Payment failed: Missing payment information.")
        return jsonify({"payment_status": "failed", "error": "Missing payment information"}), 400

    try:
        payment_status = process_payment(data["amount"], data["card_number"], data["expiry_date"], data["cvv"])
        log_event("Payment processed successfully.")
        return jsonify({"payment_status": payment_status})
    except Exception as e:
        log_event(f"Payment processing error: {str(e)}")
        return jsonify({"payment_status": "failed", "error": "Payment processing error"}), 500

# Fraud detection endpoint
@app.route('/fraud-detection', methods=['POST'])
def fraud_detection():
    data = request.get_json()
    amount = data.get("amount")
    
    if not amount:
        log_event("Fraud detection failed: No amount provided.")
        return jsonify({"fraudulent": False, "error": "No amount provided"}), 400

    is_fraud = detect_fraud(amount)
    log_event("Fraud detection executed.")
    return jsonify({"fraudulent": is_fraud})

# DDoS protection check
@app.route('/ddos-check', methods=['GET'])
def ddos_check():
    ip_address = request.remote_addr
    protection_status = ddos_protection.check_protection_status(ip_address)
    log_event(f"DDoS protection check for IP {ip_address}: {protection_status}")
    return jsonify({"message": protection_status})

# API Security endpoint (Access Secure Data)
@app.route('/secure-data', methods=['GET'])
@api_key_required
def secure_data():
    log_event("API security access attempted.")
    return jsonify({"message": "Access granted"}), 200

# Real-time Metrics for the Dashboard
@app.route('/metrics', methods=['GET'])
def metrics():
    metrics = get_real_time_metrics()
    log_event("Real-time metrics accessed.")
    return jsonify(metrics)

# Data Integrity Check endpoint
@app.route('/data-integrity-check', methods=['POST'])
def data_integrity_check():
    data = request.get_json().get("data")
    if not data:
        log_event("Data integrity check failed: No data provided.")
        return jsonify({"integrity_check": False, "error": "No data provided"}), 400

    integrity_passed = check_data_integrity(data)
    log_event("Data integrity check executed.")
    return jsonify({"integrity_check": integrity_passed})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

