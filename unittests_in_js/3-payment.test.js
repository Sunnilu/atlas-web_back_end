// 3-payment.test.js
const sinon = require('sinon');
const { expect } = require('chai');
const utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

// Test Suite for sendPaymentRequestToApi
describe('sendPaymentRequestToApi', () => {
    let spy;

    beforeEach(() => {
        // Create a spy for utils.calculateNumber
        spy = sinon.spy(utils, 'calculateNumber');
    });

    afterEach(() => {
        // Restore the original function after each test
        spy.restore();
    });

    it('should call utils.calculateNumber with SUM, 100, 20', () => {
        // Call the function with test values
        sendPaymentRequestToApi(100, 20);

        // Verify that calculateNumber was called with correct arguments
        expect(spy.calledWith('SUM', 100, 20)).to.be.true;
    });

    it('should log the correct total', () => {
        // Spying on console.log to check what is being logged
        const logSpy = sinon.spy(console, 'log');

        // Call the function with test values
        sendPaymentRequestToApi(100, 20);

        // Verify that console.log was called with the correct message
        expect(logSpy.calledWith('The total is: 120')).to.be.true;

        // Restore console.log after test
        logSpy.restore();
    });
});
