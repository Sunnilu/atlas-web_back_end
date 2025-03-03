// 5-payment.test.js

const sendPaymentRequestToAPI = require('./5-payment');
const consoleSpy = jest.spyOn(console, 'log');

describe('Payment request tests', () => {
 
  // Hook to run before each test
  beforeEach(() => {
    // Clear previous mock calls
    consoleSpy.mockClear();
  });

  // Hook to run after each test
  afterEach(() => {
    // Reset any side effects if needed
    consoleSpy.mockRestore();
  });

  it('should log the correct total when sendPaymentRequestToAPI is called with 100 and 20', () => {
    sendPaymentRequestToAPI(100, 20);

    // Check if console.log was called once
    expect(consoleSpy).toHaveBeenCalledTimes(1);

    // Check if console.log has the correct message
    expect(consoleSpy).toHaveBeenCalledWith('The total is: 120');
  });

  it('should log the correct total when sendPaymentRequestToAPI is called with 10 and 10', () => {
    sendPaymentRequestToAPI(10, 10);

    // Check if console.log was called once
    expect(consoleSpy).toHaveBeenCalledTimes(1);

    // Check if console.log has the correct message
    expect(consoleSpy).toHaveBeenCalledWith('The total is: 20');
  });
});