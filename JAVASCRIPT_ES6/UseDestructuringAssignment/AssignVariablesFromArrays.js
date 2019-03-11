let a = 8, b = 6;

// The own way
const a = (() => {
    "use strict";
    const Temp = a;
    a = b;
    b = Temp;
})();

////// ==>> use this
const newWay = (() => {
    [b, a] = [b, a];
})();

console.log(a);
console.log(b);