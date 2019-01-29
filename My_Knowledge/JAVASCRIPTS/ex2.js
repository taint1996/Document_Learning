const numbers = [1, 2, 5, 6, 8, 9, 13, 42, 65]

// devisionTwoByFilter
const devisionTwo = item => item % 2 === 0;
const devisionTwoByFilter = numbers.filter(devisionTwo);
console.log("devisionTwo by Filter", devisionTwoByFilter);

// devisionTwoByLoop
let devisionTwoByLoop = []
for(let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0)
    {
        devisionTwoByLoop.push(numbers[i]);
    }
}
console.log("devisionTwo by For Loop", devisionTwoByLoop);

// devisionTwoByReduce
const devisionTwoByReduce = numbers.reduce((acc, curr) => {
    return (curr % 2 === 0) ? [...acc, curr] : acc;
}, []);
console.log("devisionTwo by For Reduce", devisionTwoByReduce);

// Sum Numbers
const total = (acc, curr) => acc + curr;
const sumNumber = numbers.reduce(total, 0);
console.log(`Total number: ${sumNumber}`);