// 4-payment.test.js
const sinon = require('sinon');
const calculateTotal = require('./4-payment');
const Utils = require('./utils');

describe('Payment Calculation', () => {
  let calculateNumberStub;
  let logSpy;

  beforeEach(() => {
    // Stub the Utils.calculateNumber function to always return 10
    calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
   
    // Spy on console.log to ensure the correct message is logged
    logSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore the stub and spy after each test
    calculateNumberStub.restore();
    logSpy.restore();
  });

  it('should log the correct total', () => {
    calculateTotal(100, 20);

    // Verify that the stub was called with the correct parameters
    sinon.assert.calledWith(calculateNumberStub, 'SUM', 100, 20);

    // Verify that console.log was called with the expected message
    sinon.assert.calledWith(logSpy, 'The total is: 10');
  });
});