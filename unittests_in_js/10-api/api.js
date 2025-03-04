const express = require('express');
const app = express();
const router = express.Router();

app.use(express.json());
app.use('/', router);

// Helper function for payment methods response
const getPaymentMethods = () => ({
    payment_methods: {
        credit_cards: true,
        paypal: false
    }
});

// GET /available_payments endpoint
router.get('/available_payments', (req, res) => {
    res.json(getPaymentMethods());
});

// POST /login endpoint
router.post('/login', (req, res) => {
    const { userName } = req.body;
    if (!userName) {
        return res.status(400).json({ error: 'Username is required' });
    }
    res.json({ message: `Welcome ${userName}` });
});

// GET /cart/:id endpoint
router.get('/cart/:id', (req, res) => {
    const id = req.params.id;
    
    // Validate that id is a number
    if (isNaN(id) || !id.match(/^\d+$/)) {
        return res.status(404).send('Invalid cart ID');
    }
    
    // Return payment methods for valid cart ID
    const paymentMethods = `Payment methods for cart ${id}`;
    res.send(paymentMethods);
});

// Export app for testing
module.exports = router;