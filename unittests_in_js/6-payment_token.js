// 6-payment_token.js
function getPaymentTokenFromAPI(success) {
  if (success) {
      return Promise.resolve({ data: 'Successful response from the API' });
  }
  return Promise.resolve(); // Return empty promise when success is false
}

module.exports = getPaymentTokenFromAPI;