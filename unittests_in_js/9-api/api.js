// api.js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

// Add new cart endpoint with validation
app.get('/cart/:id', (req, res) => {
    const id = req.params.id;
    
    // Validate that id is a number
    if (isNaN(id) || !id.match(/^\d+$/)) {
        return res.status(404).send('Invalid cart ID');
    }
    
    // Return payment methods for valid cart ID
    const paymentMethods = `Payment methods for cart ${id}`;
    res.json(paymentMethods);
});

const PORT = 7865;
app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
});

module.exports = app;