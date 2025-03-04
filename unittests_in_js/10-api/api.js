const express = require('express');
const app = express();
// const router = express.Router();

// app.use(express.json());
// app.use('/', router);

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

// Helper function for payment methods response
const paymentMethods = {
    payment_methods : {
        credit_cards: true,
        paypal: false
    }
};

// GET /available_payments endpoint
app.get('/available_payments', (req, res) => {
    res.json(paymentMethods);
});

// POST /login endpoint
app.post('/login', (req, res) => {
    const userName = req.body.userName;
    if (!userName) {
        return res.status(400).json({ error: 'Username is required' });
    }
    res.json({ message: `Welcome ${userName}` });
});

// GET /cart/:id endpoint
app.get('/cart/:id', (req, res) => {
    const id = req.params.id;
    
    // Validate that id is a number
    if (isNaN(id) || !id.match(/^\d+$/)) {
        return res.status(404).send('Invalid cart ID');
    }
    
    // Return payment methods for valid cart ID
    const paymentMethods = `Payment methods for cart ${id}`;
    res.send(paymentMethods);
});

const PORT = 7865;
app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
});

// Export app for testing
module.exports = app;