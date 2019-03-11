const iceCreams = [
    { flavor: 'pineapple', color: 'white' },
    { flavor: 'strawberry', color: 'red' },
    { flavor: 'watermelon', color: 'red' },
    { flavor: 'kiwi', color: 'green' },
    { flavor: 'mango', color: 'yellow' },
    { flavor: 'pear', color: 'green' }
];

//////// Using Filter()
const getRed = iceCream => iceCream.color === "red";
// Let’s use the filter method to create a new array with only red colored ice cream.
const favoriteFlavors = iceCreams.filter(getRed);
console.log(favoriteFlavors);


//////// Using Map()
// Before we use map() let’s try doing it the old school way with a classic for loop.
let flavors = [];

for (let i = 0; i < iceCreams.length; i++) {
    flavors.push(iceCreams[i].flavor);
}
console.log(flavors);

// Let’s try the same thing with the map() method.
const getAllFlavor = iceCreams.map(iceCream => iceCream.flavor);
console.log("Get All Flavor", getAllFlavor);

///////// Using Reduce() 
/* Finally! As Christian Sakai mentioned in a previous comment, 
    reduce is the granddad / grandma of all of these methods */


const arr = [10, 20, 30];
// First with for loop
let S = 0;
for (let i = 0; i < arr.length; i++){
    S += arr[i];
}
console.log(S);
// Now use Reduce
const reducerFunction = (accumulator, currentValue) => accumulator + currentValue;

const sumArr = arr.reduce(reducerFunction, 0);
console.log(`Total Arr: ${sumArr}`);