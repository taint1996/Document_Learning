// The some() method tests whether at least one element 
    // in the array passes the test implemented by the provided function.
const ages = [ 23, 32, 17, 19, 34];

const agesOverThan15 = i => (i > 25);
const someAgeOver15 = ages.some(agesOverThan15);
console.log("some Element Age Is Over 25: ", ageIsOver15);

const checkWhetherElementIsEven = ages.some(i => i % 2 == 0);
console.log("check Whether Element Is Even: ", checkWhetherElementIsEven);