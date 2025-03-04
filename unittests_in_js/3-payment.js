// 3-payment.js
const utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const result = utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${result}`);  // Changed 'total' to 'result'
}

module.exports = sendPaymentRequestToApi;
