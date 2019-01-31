// Basic JavaScript: Generate Random Fractions with JavaScript: Tạo phân số ngẫu nhiên với JavaScript
const randomNumber = () => {
    return Math.random();
}

// Generate Random Whole Numbers with JavaScript: tạo số nguyên ngẫu nhiên bằng JavaScript
var randomNumber0and9 = Math.floor(Math.random() * 10);
function randomWholeNum() {
    // Only change code below this line.
    return randomNumber0and9;
}

const randomNumber0and19 = () => Math.floor(Math.random() * 20);
console.log(randomNumber0and19());


// Generate Random Whole Numbers within a Range: Tạo số nguyên ngẫu nhiên trong một phạm vi
function ourRandomRange(ourMin, ourMax) {
    return Math.floor(Math.random() * (ourMax - ourMin + 1)) + ourMin;
}

ourRandomRange(1, 9);

function randomRange(myMin, myMax) {
    return Math.floor(Math.random() * (Math.max(myMax) - Math.min(myMin) + 1) + Math.min(myMin));
}

var myRandom = randomRange(10, 15);


// Basic JavaScript: Use the parseInt Function to convert to Integer
const convertToInteger = (str) => parseInt(str);
console.log(convertToInteger("56")); // -> 56

// Basic JavaScript: Use the parseInt Function with a Radix: sử dụng parseInt with Redix
const convertIntegerWithRedix = (str) => {
    return parseInt(str, 2);
}
console.log("Use parseInt with Redix: ", convertIntegerWithRedix("10011")); // -> 19
