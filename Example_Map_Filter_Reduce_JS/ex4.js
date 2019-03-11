const words = ["spray", "limit", "elite", "exuberant", "destruction", "present"];

// check item > 6
const longWordsGratherThanSix = words.filter(item => item.length > 6);
console.log("Long words grather than six:", longWordsGratherThanSix);

const longWords = words.reduce((acc, curr) => (curr.length > 6) ? [...acc, curr] : acc, []);
console.log("long Words: ", longWords);