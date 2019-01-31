// Push the numbers 0 through 4 to myArray using a while loop.

//////////////////////////////// While Loop ////////////////////////////////
// Setup
var myArray = [];

var i = 0;
while (i < 5) {
    myArray.push(i);
    i++;
}

//////////////////////////////// For Loop ////////////////////////////////
// Setup
var forLoopArray = [];

for (var i = 1; i <= 5; i++) {
    forLoopArray.push(i);
}

// Push the odd numbers from 1 through 9 to myArray using a for loop.
for (var i = 0; i < 10; i++)
{
    if (i % 2 !== 0)
    {
        myArray.push(i);
    }
}

// Push the odd numbers from 9 through 1 to myArray using a for loop.

for (var i = 10; i > 0; i--) {
    if (i % 2 !== 0) {
        myArray.push(i);
    }
}

// Declare and initialize a variable total to 0. Use a for loop to add the value of each element of the myArr array to total.
var myArr = [ 2, 3, 4, 5, 6];
var total = 0;

for (var i = 0; i < myArr.length; i++) {
    total += myArr[i];  
}

const totalReduce = myArr.reduce((acc, curr) => acc + curr, 0);
console.log("Total Map", totalMap);

//// Nesting For Loops: Modify function multiplyAll so that it multiplies the product variable by each number in the sub-arrays of arr
function multiplyAll(arr) {
    var product = 1;
    // Only change code below this line
    for (var i = 0; i < arr.length; i++)
    {
        for (var j = 0; j < arr[i].length; j++) {
          product *= arr[i][j];
        }
    }
    // Only change code above this line
    return product;
    }

    // Modify values below to test your code
multiplyAll([[1, 2], [3, 4], [5, 6, 7]]);

//////// do...while Loop
do {
    myArray.push(i);
    i++;
} while (i < 5);