// Encrypt data
function encryptData() {
    const data = document.getElementById("dataToEncrypt").value;
    fetch("/encrypt", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: data })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("encryptionResult").innerText = "Encrypted Data: " + data.encrypted_data;
    });
}

// Authenticate user
function authenticateUser() {
    const userId = document.getElementById("userId").value;
    const password = document.getElementById("password").value;
    fetch("/authenticate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: userId, password: password })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("authResult").innerText = data.authenticated ? "Authenticated" : "Authentication Failed";
    });
}

// Process payment
function processPayment() {
    const amount = document.getElementById("amount").value;
    const cardNumber = document.getElementById("cardNumber").value;
    const expiryDate = document.getElementById("expiryDate").value;
    const cvv = document.getElementById("cvv").value;
    fetch("/payment", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ amount, card_number: cardNumber, expiry_date: expiryDate, cvv })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("paymentResult").innerText = data.payment_status;
    });
}
