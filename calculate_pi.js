// Leibniz formula: pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
function calculatePi(decimalPlaces = 5) {
    const tolerance = 0.5 * Math.pow(10, -(decimalPlaces + 1));
    let pi = 0;
    let denominator = 1;
    let sign = 1;

    while (true) {
        const term = sign / denominator;
        pi += term;
        if (Math.abs(term) < tolerance) break;
        sign *= -1;
        denominator += 2;
    }

    return (pi * 4).toFixed(decimalPlaces);
}

console.log(`pi = ${calculatePi(5)}`);
