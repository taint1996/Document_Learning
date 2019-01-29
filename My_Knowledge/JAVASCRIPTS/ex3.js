const input = [[1, 2, 3], [4, 5, 6]];

const output = input.reduce((acc, curr) => [...acc, ...curr], []);
console.log("Spreed input: ", output);