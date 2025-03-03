// 1-calcul.test.js

const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('SUM operation', function () {
    it('should add rounded numbers correctly', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 2.6), 4);
    });

    it('should handle negative numbers', function () {
      assert.strictEqual(calculateNumber('SUM', -1.4, -2.6), -4);
    });

    it('should handle edge case of rounding down', function () {
      assert.strictEqual(calculateNumber('SUM', 0.4, 0.4), 0);
    });
  });

  describe('SUBTRACT operation', function () {
    it('should subtract rounded numbers correctly', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 5.6, 2.4), 3);
    });

    it('should handle negative results correctly', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 2.6), -1);
    });
  });

  describe('DIVIDE operation', function () {
    it('should divide rounded numbers correctly', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 7.6, 2.4), 3.1666666666666665);
    });

    it('should handle division by zero', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 7.6, 0), 'Error');
    });

    it('should return "Error" if b is 0 after rounding', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 5.1, 0), 'Error');
    });
  });

  describe('Invalid operation type', function () {
    it('should return "Invalid operation type" for an unsupported type', function () {
      assert.strictEqual(calculateNumber('MULTIPLY', 1, 2), 'Invalid operation type');
    });
  });
});