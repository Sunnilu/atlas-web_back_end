// hbtn_test_0.test.js
const sinon = require('sinon');
const { expect } = require('chai');
const utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

// Test Suite for Utils.calculateNumber
describe('Utils.calculateNumber', () => {
    let spy;

    beforeEach(() => {
        // Create a spy for utils.calculateNumber
        spy = sinon.spy(utils, 'calculateNumber');
    });

    afterEach(() => {
        // Restore the original function after each test
        spy.restore();
    });

    it('should round the first argument when type is SUM', () => {
        // Rounding should occur when passing 1.3 and 1.4
        const result = utils.calculateNumber('SUM', 1.3, 1.4);
        expect(result).to.equal(2);  // rounded to 2
    });

    it('should round the second argument when type is SUM', () => {
        // Ensure rounding on the second argument
        const result = utils.calculateNumber('SUM', 1.4, 1.3);
        expect(result).to.equal(2);  // rounded to 2
    });

    it('should return the correct number when type is SUM', () => {
        const result = utils.calculateNumber('SUM', 1.3, 1.4);
        expect(result).to.equal(2);  // rounded to 2
    });

    it('should round the first argument when type is SUBTRACT', () => {
        const result = utils.calculateNumber('SUBTRACT', 1.4, 1.3);
        expect(result).to.equal(0);  // rounded to 0
    });

    it('should round the second argument when type is SUBTRACT', () => {
        const result = utils.calculateNumber('SUBTRACT', 1.3, 1.4);
        expect(result).to.equal(-0);  // rounded to 0
    });

    it('should return the correct number when type is SUBTRACT', () => {
        const result = utils.calculateNumber('SUBTRACT', 2.4, 1.4);
        expect(result).to.equal(1);  // correct result
    });

    it('should round the first argument when type is DIVIDE', () => {
        const result = utils.calculateNumber('DIVIDE', 5.5, 10);
        expect(result).to.equal(0.5);  // rounded result
    });

    it('should round the second argument when type is DIVIDE', () => {
        const result = utils.calculateNumber('DIVIDE', 10, 5.5);
        expect(result).to.equal(1.8);  // rounded result
    });

    it('should return the correct number when type is DIVIDE', () => {
        const result = utils.calculateNumber('DIVIDE', 10, 5);
        expect(result).to.equal(2);  // correct result
    });

    it('should throw an error when dividing by 0', () => {
        // Ensure an error is thrown when dividing by zero
        expect(() => utils.calculateNumber('DIVIDE', 5, 0)).to.throw('Cannot divide by 0');
    });
});

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
