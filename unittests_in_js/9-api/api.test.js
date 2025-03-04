const request = require('request');
const chai = require('chai');
const expect = chai.expect;
describe('Index page', function() {
    const url = 'http://localhost:7865/cart/';
    it('should return status 200', function(done) {
        request(url + '1', function(error, response, body) {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });
    it('should return 404 with wrong id type', function(done) {
        request(url + 'a', function(error, response, body) {
            expect(response.statusCode).to.equal(404);
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