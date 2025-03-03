const { expect } = require('chai');
const { add, subtract } = require('./2-calcul_chai');

describe('Math functions', function() {
  describe('#add()', function() {
    it('should return the sum of two numbers', function() {
      const result = add(1, 2);
      expect(result).to.equal(3); // Using Chai's expect style
    });
  });

  describe('#subtract()', function() {
    it('should return the difference between two numbers', function() {
      const result = subtract(5, 3);
      expect(result).to.equal(2); // Using Chai's expect style
    });
  });
});
