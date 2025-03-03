// 5-payment.test.js
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToAPI = require('./5-payment');

describe('sendPaymentRequestToAPI', () => {
    let consoleSpy;

    beforeEach(() => {
        // Create a single spy for console.log that will be used across all tests
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        // Restore the original console.log behavior after each test
        consoleSpy.restore();
    });

    it('should log total of 120 when given 100 and 20', () => {
        sendPaymentRequestToAPI(100, 20);
        
        // Verify the exact message was logged
        sinon.assert.calledWith(consoleSpy, 'The total is: 120');
        
        // Verify console.log was called exactly once
        sinon.assert.calledOnce(consoleSpy);
    });

    it('should log total of 20 when given 10 and 10', () => {
        sendPaymentRequestToAPI(10, 10);
        
        // Verify the exact message was logged
        sinon.assert.calledWith(consoleSpy, 'The total is: 20');
        
        // Verify console.log was called exactly once
        sinon.assert.calledOnce(consoleSpy);
    });
});