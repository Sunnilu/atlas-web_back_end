// 4-payment.test.js
const sinon = require('sinon');
const calculateTotal = require('./4-payment');
const Utils = require('./utils');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToAPI with stubs', () => {
  let calculateNumberStub;
  let consoleSpy;

  beforeEach(() => {
    // Stub the Utils.calculateNumber function to always return 10
    calculateNumberStub = sinon.spy(console, 'log'); // spy on console.log
  });

  afterEach(() => {
    // Restore the stub and spy after each test
    calculateNumberStub.restore();
    console.restore();
  });

  it('validates that Utils.calculateNumber was called with the right arguments and sonsole.log with the correct message', () => {
    sendPaymentRequestToApi(100, 20);

    // Verify that the stub was called with the correct parameters
    expect(calculateNumberStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true

    // Verify that console.log was called with the expected message
    expect(consoleSpy.calledOnceWithExactly(' The total is: 10')).to.be.true;
  });
});