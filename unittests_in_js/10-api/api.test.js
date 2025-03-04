const request = require('request');
const app = require('./api');
const chai = require("chai");
const expect = chai.expect;

describe('API Endpoints', () => {
    // Available Payments Tests
    describe('GET /available_payments', () => {
        it('should return payment methods', (done) => {
            request.get('http://localhost:7865/available_payments', 
                { json: true }, 
                (error, response, body) => {
                    expect(response.statusCode).to.equal(200);
                    // expect(body).toHaveProperty('payment_methods');
                    // expect(body.payment_methods).toEqual({
                    //     credit_cards: true,
                    //     paypal: false
                    // });
                    done();
                }
            );
        });
    });

    // Login Tests
    describe('POST /login', () => {
        it('should return welcome message with valid username', (done) => {
            const option = {
                url: 'http://localhost:7865/login',
               method: 'POST',
                body: { userName: 'Betty' }
            }, 
            (error, response, body) => {
                expect(response.statusCode).toBe(200);
                expect(body).toHaveProperty('message');
                expect(body.message).toBe('Welcome testUser');
                done();
            });
        });

        it('should return error for missing username', (done) => {
            request.post({
                url: 'http://localhost:7865/login',
                json: true,
                body: {}
            }, 
            (error, response, body) => {
                expect(response.statusCode).toBe(400);
                expect(body).toHaveProperty('error');
                expect(body.error).toBe('Username is required');
                done();
            });
        });
    });
});