const myArray = [20, 120, 111, 215, 54, 78];
const sumArray = myArray.reduce((acc, curr) => {
  acc += curr
  return acc;
}, 0);

//// find Max Element of Array
const findMax = Math.max(...myArray);

//// find Min Element of Array
const findMin = Math.min(...myArray);

// find Event Element
const findEvenElement = myArray.filter(i => i % 2 === 0);

// count all even element of array
const totalEvenElement = () => {
  let count = 0;

  for(let i = 0; i < myArray.length; i++) {
    if (myArray[i] % 2 == 0) {
      count++;
    }
  }
  return count;
}

// find odd element of myArray
const findOddElement = myArray.filter(i => i % 2 !== 0);
const totalOddElement = () => {
  let count = 0;

  for (let i = 0; i < myArray.length; i++) {
    count++;
  }
  return count;
}

const secondMax = () => {
  const max = Math.max.apply(null, arr);  
  arr.splice(arr.indexOf(max), 1);
  return Math.max.apply(arr, arr);
}
console.log("second Max in Array is ", secondMax);


// count Negative number
const countNegative = myArray.reduce((count, currentValue) => {
  if (currentValue < 0) {
    count++;
  }
  return count;
}, 0)
console.log("count Negative", countNegative)