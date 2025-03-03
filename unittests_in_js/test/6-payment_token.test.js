// 6-payment_token.test.js

const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {

  it('should return successful response when success is true', (done) => {
    // Call the function with 'true' to simulate a successful response
    getPaymentTokenFromAPI(true).then((response) => {
      // Test if the response contains the expected data
      expect(response).toEqual({ data: 'Successful response from the API' });
     
      // Call done() to let Jest know the async test is complete
      done();
    }).catch((error) => {
      // If there is an error, fail the test
      done(error);
    });
  });

  it('should not return any response when success is false', (done) => {
    // Call the function with 'false' to simulate no response
    getPaymentTokenFromAPI(false).then((response) => {
      // Expect that no response is returned
      expect(response).toBeUndefined();

      // Call done() to indicate the test is complete
      done();
    }).catch((error) => {
      // If there is an error, fail the test
      done(error);
    });
  });

});