// Business logic - add and subtract functions
function add(a, b) {
    return a + b;
  }
  
  function subtract(a, b) {
    return a - b;
  }
  
  // Test suite using Chai's expect for BDD-style tests
  const { expect } = require('chai');
  
  
    describe('#subtract()', function() {
      it('should return the difference between two numbers', function() {
        const result = subtract(5, 3);
        expect(result).to.equal(2); // Chai's expect style
      });
    });
  
  // Export the functions for testing purposes
  module.exports = { add, subtract };
  