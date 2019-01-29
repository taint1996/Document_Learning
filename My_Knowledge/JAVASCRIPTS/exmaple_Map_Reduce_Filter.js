const numbers = [1, 4, 6, 9]

// double forloop
let byTwo = [];

for (let i = 0; i < numbers.length; i++) {
    byTwo.push(numbers[i] * 2);    
}
console.log("By Two for Loop", byTwo);

const doubleByMap = numbers.map(item => item * 2);
console.log("doubleByMap", doubleByMap);

const doubleByReduce = numbers.reduce((acc, curr) => acc = acc[curr] * 2 , 0);
console.log("doubleByReduce", doubleByMap);
