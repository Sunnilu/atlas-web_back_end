const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('Math functions', function() {
  describe('#add()', function() {
    it('should return the sum of two numbers', function() {
      const result = calculateNumber('SUM', 2, 3);
      expect(result).to.equal(5); // Using Chai's expect style
    });
  });

  describe('#subtract()', function() {
    it('should return the difference between two numbers', function() {
      const result = calculateNumber('SUBTRACT', 5, 3);
      expect(result).to.equal(2); // Using Chai's expect style
    });
  });
});
