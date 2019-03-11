// The every() method tests whether all elements in the array
    //  pass the test implemented by the provided function.
var ages = [ 23, 32, 17, 19, 34 ]

const everyAgesIsOver15 = ages.every(i => (i > 15));

const twentyOneOrAbove = i => (i >= 21);
const isEveryTwentyOneOrAbove = ages.every(twentyOneOrAbove);
console.log("isEveryTwentyOneOrAbove:", twentyOneOrAbove);