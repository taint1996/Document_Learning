// [[a, b, c], [d, e, f], [g, h i]] -> [a, b, c, d, e, f, g, h, i]
const letterArr = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']];
const out = letterArr.reduce((acc, curr) => { return acc.concat(curr) }, []);
console.log("Output", out);

const numberArr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
const outputs = numberArr.reduce((acc, curr) => [...acc, ...curr], []);
console.log("output Number Arr", outputs);

// return a new array with all value as multiple of 10 by map, reduce;
const multipleOfTenByReduce = outputs.reduce((acc, curr) => {
    acc.push(curr * 10);
    return acc;
}, []);

const multipleOfTenByMap = outputs.map(i => i * 10);

// using Splice on Array
var array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
var removed = array.splice(2, 1); // => [1,2,4,5,6,7,8,9,0]
