//1-calcul.js

function calculateNumber(a, b) {
    // round both numbers and return their sum
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);

    if (type === 'SUM') {
        return roundedA + roundedB;
    }
    else if (type === 'SUBTRACT') {
        return roundedA - roundedB;
    }
    else if (type === 'DIVIDE') {
        if (roundedB === 0) {
            return 'Error';
        }
        return roundedA / roundedB;
    }
    else {
        return 'Invalid operation type'; // in case of a invalid operation type
    }
}

module.exports = calculateNumber;