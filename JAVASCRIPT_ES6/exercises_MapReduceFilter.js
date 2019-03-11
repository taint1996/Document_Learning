const flavours = [
    "strawberry",
    "strawberry",
    "kiwi",
    "kiwi",
    "kiwi",
    "strawberry",
    "mango",
    "kiwi",
    "banana"
];

// This out will amount total every flavour
const output = flavours.reduce((acc, curr) => {
    !acc[curr] ? acc[curr] = 1 : acc[curr] += 1;
    return acc;
}, {});
console.log("OP", output)

// Ex2 : Flattening data with reduce
const data = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]; // -> [a, b, c, d, e, f, g, h, i];
const reduceData = data.reduce((acc, curr) => {
    return (acc.concat(curr));
}, []);
console.log("reduceData", reduceData);

// Ex3: Performance with list transformers
let bigData = [];
for (let i = 0; i < 1000000; i++) {
  bigData[i] = i;
}

// Compare time spend with filter map vs reduce

//// Filter Map is slow => 0.77s
let filterBegin = Date.now();
const mapReduce = bigData.filter(i => i % 2 === 0).map(i => i * 2);
let filterEnd = Date.now();
let filterTimeSpent = (filterEnd - filterBegin) / 1000 + "sec";

// Fast performence
let reducedBegin = Date.now();
let reduceBigData = bigData.reduce((acc, curr) => {
    if (curr % 2 === 0) {
        acc.push(curr * 2);
    }
    return acc;
}, []);
let reducedEnd = Date.now();
let showTime = (reducedEnd - reducedBegin) / 1000 + "secs" // only 0.017s