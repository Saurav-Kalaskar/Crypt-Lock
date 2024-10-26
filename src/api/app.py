import os
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
from src.core.encryption import encrypt_data
from src.core.auth import authenticate_user
from src.core.payments import process_payment
from src.monitoring.logger import log_event

# Load environment variables
load_dotenv()

# Initialize Flask app with template and static folder locations
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    log_event("Health check requested.")
    return jsonify({"status": "OK", "message": "Server is running"}), 200

# Home route for the UI
@app.route('/')
def index():
    return render_template('index.html')

# Encryption route
@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json().get("data", "Sample data to encrypt")
    encrypted_data = encrypt_data(data)
    return jsonify({"encrypted_data": encrypted_data})

# Authentication route
@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    user_id = data.get("user_id")
    password = data.get("password")
    auth_status = authenticate_user(user_id, password)
    return jsonify({"authenticated": auth_status})

# Payment processing route
@app.route('/payment', methods=['POST'])
def payment():
    data = request.get_json()
    amount = data.get("amount")
    card_number = data.get("card_number")
    expiry_date = data.get("expiry_date")
    cvv = data.get("cvv")
    payment_status = process_payment(amount, card_number, expiry_date, cvv)
    return jsonify({"payment_status": payment_status})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
