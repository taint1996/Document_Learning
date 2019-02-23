const realNumberArray = [4, 5.6, -9.8, 3.14, 42, 6, 8.34, -2];
const squareList = (arr) => {
    "use strict";
    // change code below this line: use Map Filter
    //    const squaredIntegers = arr.filter(item => (Number.isInteger(item) && item > 0)).map(i => i ** 2);
    // use Reduce
    const squaredIntegers = arr.reduce((acc, curr) => {
        if (Number.isInteger(curr) && curr > 0) {
            acc.push(curr ** 2);            
        }
        return acc;
    }, []);

    return squaredIntegers;
};
// test your code
const squaredIntegers = squareList(realNumberArray);
console.log(squaredIntegers);