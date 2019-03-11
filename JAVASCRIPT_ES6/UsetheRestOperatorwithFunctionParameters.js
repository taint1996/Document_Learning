// Use the Rest Operator with Function Parameters
// In order to help us create more flexible functions, 
    // ES6 introduces the rest operator for function parameters. 
    // With the rest operator, you can create functions that take a variable number of arguments. 
    // These arguments are stored in an array that can be accessed later from inside the function.
const sum = (function() {
    "use strict";

    return function sum(...args) {
        return args.reduce((acc, curr) => acc + curr, 0);
    }
})();
console.log((sum(1,2,3)));
// The rest operator eliminates the need to check the args array and allows us to apply map(), filter() and reduce() on the parameters array.
