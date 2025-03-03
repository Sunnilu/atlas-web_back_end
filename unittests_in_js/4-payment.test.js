// 4-payment.test.js
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
    let calculateNumberStub;
    
    beforeEach(() => {
        // Create a stub that returns 10 for any input
        calculateNumberStub = sinon.stub(Utils, 'calculateNumber')
            .returns(10);
        
        // Create a spy for console.log
        sinon.spy(console, 'log');
    });

    afterEach(() => {
        // Clean up after each test
        calculateNumberStub.restore();
        console.log.restore();
    });

    it('should call calculateNumber with correct parameters', () => {
        sendPaymentRequestToApi(100, 20);
        
        // Verify the stub was called with correct parameters
        sinon.assert.calledWith(calculateNumberStub, 'SUM', 100, 20);
    });

    it('should log correct message', () => {
        sendPaymentRequestToApi(100, 20);
        
        // Verify console.log was called with the expected message
        sinon.assert.calledWith(console.log, 'The total is: 10');
    });
});