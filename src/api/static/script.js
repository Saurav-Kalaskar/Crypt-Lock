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
        document.getElementById("encryptionResult").innerText = "Encrypted Data: " + (data.encrypted_data || "Error encrypting data");
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("encryptionResult").innerText = "Error encrypting data";
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
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("authResult").innerText = "Error during authentication";
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
        document.getElementById("paymentResult").innerText = data.payment_status || "Error processing payment";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("paymentResult").innerText = "Error processing payment";
    });
}

// Fraud Detection
function detectFraud() {
    const transactionAmount = document.getElementById("transactionAmount").value;
    fetch("/fraud-detection", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ amount: transactionAmount })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("fraudResult").innerText = data.fraudulent ? "Fraud Detected" : "No Fraud Detected";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("fraudResult").innerText = "Error detecting fraud";
    });
}

// DDoS Protection
function simulateDDoSProtection() {
    fetch("/ddos-check", { method: "GET" })
    .then(response => response.json())
    .then(data => {
        document.getElementById("ddosResult").innerText = data.message || "Error in DDoS protection check";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("ddosResult").innerText = "Error in DDoS protection check";
    });
}

// API Security (Access Secure Data)
function accessSecureData() {
    fetch("/secure-data", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "API-Key": "SECURE_API_KEY"  
        }
    })
    .then(response => {
        if (!response.ok) throw new Error("Access Denied");
        return response.json();
    })
    .then(data => {
        document.getElementById("apiResult").innerText = data.message || "Access Denied";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("apiResult").innerText = "Error accessing secure data";
    });
}


// Real-Time Metrics

function getRealTimeMetrics() {
    fetch("/metrics", { method: "GET" })
    .then(response => response.json())
    .then(data => {
        document.getElementById("metricsResult").innerText = `CPU: ${data.cpu_usage || "--"}%, Memory: ${data.memory_usage || "--"}%`;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("metricsResult").innerText = "Error retrieving metrics";
    });
}

// Auto-refresh metrics every 5 seconds
setInterval(getRealTimeMetrics, 5000);


// Data Integrity Check
function checkDataIntegrity() {
    const data = document.getElementById("dataToCheck").value;
    fetch("/data-integrity-check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: data })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("dataIntegrityResult").innerText = data.integrity_check ? "Data Integrity Passed" : "Data Integrity Failed";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("dataIntegrityResult").innerText = "Error checking data integrity";
    });
}
