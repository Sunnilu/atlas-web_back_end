const { expect } = require('chai');
const Utils = require('./utils');

describe('Utils.calculateNumber', () => {
  // ... your other tests ...

  it('should round the first argument when type is DIVIDE', () => {
    expect(Utils.calculateNumber('DIVIDE', 5.6, 10)).to.be.closeTo(0.6, 0.1);
  });

  it('should round the second argument when type is DIVIDE', () => {
    expect(Utils.calculateNumber('DIVIDE', 10, 5.4)).to.be.closeTo(1.8, 0.1);
  });

  // ... your other tests ...
});