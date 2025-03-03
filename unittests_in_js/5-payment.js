//5-payment.js

function sendPaymentRequestToAPI(totalAmount, shippingCost) {
    const total = totalAmount + shippingCost;
    console.log(`The total is: ${total}`);
}

module.exports = sendPaymentRequestToAPI;
