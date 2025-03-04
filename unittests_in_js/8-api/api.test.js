const request = require('request');
const chai = require('chai');
const expect = chai.expect;
describe('Index page', function() {
    const url = 'http://localhost:7865/';
    it('should return status 200', function(done) {
        request(url, function(error, response, body) {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });
    it('should return Welcome to the payment system', function(done) {
        request(url, function(error, response, body) {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
    it('should return correct content-type header', function(done) {
        request(url, function(error, response, body) {
            expect(response.headers['content-type']).to.include('text/html');
            done();
        });
    });
});