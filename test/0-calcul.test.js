// 0-calcul.test.js
// const assert = require('assert');
// const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('should return the sum of 2 rounded numbers', function() {
    assert.strictEqual(calculateNumber(1.4, 2.6), 4);
    assert.strictEqual(calculateNumber(1.2, 3.8), 5);
    assert.strictEqual(calculateNumber(1.5, 3.5), 5);
    assert.strictEqual(calculateNumber(1.4, 3.4), 4);
    assert.strictEqual(calculateNumber(0.0, 0), 0);
  });
});