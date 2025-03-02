// utils.js
function calculateNumber(type, a, b) {
    // Simulating an expensive calculation
    if (type === 'SUM') {
      return a + b;
    }
    return 0;
  }
  
  module.exports = {
    calculateNumber,
  };