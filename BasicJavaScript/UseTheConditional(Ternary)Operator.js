//// Ternary Operation
const checkEqual = (a, b) => {
    return (a === b) ? true : false;
}
console.log("Check Equal: ", checkSign(1, 2));

// Use multiple conditional operators in the checkSign function to check if a number is positive, negative or zero.
const checkSign = (num) => {
    return (num > 0) ? "positive" : (num < 0) ? "negative" : "zero";
}
console.log("Check Sign: ", checkSign(15));
