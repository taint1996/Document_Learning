// ES6 introduces the spread operator,
//  which allows us to expand arrays and other expressions in places where multiple parameters or elements are expected.
// in the ES 5 uses apply() to compute the maximum value in an array:
var arr = [6, 89, 3, 45];
var maximus = Math.max.apply(null, arr); // return 89
// We had to use Math.max.apply(null, arr) because Math.max(arr) returns NaN. Math.max() expects comma-separated arguments, but not an array.


///////// | use this
//    v
///////// The spread operator makes this syntax much better to read and maintain.
const arr = [6, 89, 3, 45];
const maxES6 = Math.max(...arr);

// Ex2: Copy all contents of arr1 into another array arr2 using the spread operator.
const arr1 = ['JAN', 'FEB', 'MAR', 'APR', 'MAY'];
let arr2;
(function () {
    "use strict";
    arr2 = [...arr1]; // change this line
})();
console.log(arr2);

// Use Destructuring Assignment to Assign Variables from Objects
const AVG_TEMPERATURES = {
    today: 77.5,
    tomorrow: 79
};

const getTempOfTomorrow = (avgTempurator) => {
    "use strict";
    const { tomorrow: tempOfTomorrow } = avgTempurator;
    return tempOfTomorrow;
};
console.log("temp of tomorrow", getTempOfTomorrow(AVG_TEMPERATURES));