// ************* Map with Reduce: Tripple element *************
const data = [10, 20, 30];

const trippleElement = item => item * 3;
const trippleWithMap = data.map(trippleElement)

const trippleWithReduce = data.reduce((accumulator, currentValue) => {
    accumulator.push(currentValue * 3);
    return accumulator;
}, []);
console.log(`Tripple Element by Map: ${trippleWithMap} - by Reduce: ${trippleWithReduce}`);

