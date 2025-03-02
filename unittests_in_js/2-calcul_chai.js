// Business logic - add and subtract functions
function add(a, b) {
    return a + b;
  }
  
  function subtract(a, b) {
    return a - b;
  }
  
  // Test suite using Chai's expect for BDD-style tests
  const { expect } = require('chai');
  
  // Test cases
  describe('Math functions', function() {
    describe('#add()', function() {
      it('should return the sum of two numbers', function() {
        const result = add(1, 2);
        expect(result).to.equal(3); // Chai's expect style
      });
    });
  
    describe('#subtract()', function() {
      it('should return the difference between two numbers', function() {
        const result = subtract(5, 3);
        expect(result).to.equal(2); // Chai's expect style
      });
    });
  });
  
  // Export the functions for testing purposes
  module.exports = { add, subtract };
  