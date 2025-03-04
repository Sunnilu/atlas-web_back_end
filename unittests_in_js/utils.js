// utils.js (example)
function calculateNumber(type, a, b) {
  a = Math.round(a);  // Round a
  b = Math.round(b);  // Round b

  if (type === 'SUM') {
      return a + b;
  } else if (type === 'SUBTRACT') {
      return a - b;
  } else if (type === 'DIVIDE') {
      if (b === 0) {
          throw new Error('Cannot divide by 0');
      }
      // Round the result to 1 decimal place
      return Math.round((a / b) * 10) / 10;
  }
}

module.exports = { calculateNumber };
