const express = require('express');
const app = express();
app.use(express.json());

// Existing routes remain unchanged...

// GET /available_payments endpoint
app.get('/available_payments', (req, res) => {
    res.json({
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    });
});

// POST /login endpoint
app.post('/login', (req, res) => {
    const { userName } = req.body;
    if (!userName) {
        return res.status(400).json({ error: 'Username is required' });
    }
    res.json({ message: `Welcome ${userName}` });
});

// Export app for testing
module.exports = app;