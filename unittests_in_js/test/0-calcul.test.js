const assert = require('assert');
const calculateNumber = require('../0-calcul');

describe('calculateNumber', function () {
  it('should round both numbers and return the sum', function () {
    assert.strictEqual(calculateNumber(1.4, 2.6), 4);
  });

  it('should round negative numbers and return the sum', function () {
    assert.strictEqual(calculateNumber(-1.4, -2.6), -4);
  });

  it('should round 0 to 0 and return the sum', function () {
    assert.strictEqual(calculateNumber(0.4, 0.4), 0);
  });

  it('should handle large numbers', function () {
    assert.strictEqual(calculateNumber(1234.5678, 8765.4321), 10000);
  });

  it('should handle exact integers without rounding', function () {
    assert.strictEqual(calculateNumber(3, 5), 8);
  });

  it('should round down and return correct sum for small fractional numbers', function () {
    assert.strictEqual(calculateNumber(0.1, 0.1), 0);
  });

  it('should handle edge case of rounding to nearest integer', function () {
    assert.strictEqual(calculateNumber(2.5, 2.5), 5);
  });
});