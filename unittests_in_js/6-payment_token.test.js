// 6-payment_token.test.js
const sinon = require('sinon');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
    it('should return the expected data when success is true', (done) => {
        getPaymentTokenFromAPI(true)
            .then((result) => {
                sinon.assert.match(result, { data: 'Successful response from the API' });
                done();
            })
            .catch((error) => {
                done(error);
            });
    });
});