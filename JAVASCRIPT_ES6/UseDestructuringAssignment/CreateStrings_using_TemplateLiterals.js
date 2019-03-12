// Create Strings using Template Literals
// A new feature of ES6 is the template literal. This is a special type of string that makes creating complex strings easier.
// Template literals allow you to create multi-line strings and to use string interpolation features to create strings.
const person = {
    name: "Tai Big Boy",
    age: 23
}
const greeting = `Hello, my name is ${person.name}!
I'm ${person.age} years old`;
console.log(greeting);

const cat = {
    name: 'Kitty',
    age: 3,
    paws: 4,
    whiskers: 50,
    colour: 'black',
};

const dog = {
    name: 'Doggy',
    age: 4,
    paws: 4,
    "tail-type": 'short',
    colour: 'white',
};

function nameAndPaws(animal) {
    return `${animal.name}, has ${animal.paws} paws!`;
}
console.log(nameAndPaws(cat, dog));

// Challenge
const result = {
    success: ["max-length", "no-amd", "prefer-arrow-functions"],
    failure: ["no-var", "var-on-top", "linebreak"],
    skipped: ["id-blacklist", "no-dup-keys"]
};

// Write code above 
const makeList = (arr) => {
    const resultDisplayArray = arr.map(value => {
        return `<li class="text-warning">${value}</li>`;
    })
    return resultDisplayArray;
}
//

/**
 * makeList(result.failure) should return:
 * [ `<li class="text-warning">no-var</li>`,
 *   `<li class="text-warning">var-on-top</li>`, 
 *   `<li class="text-warning">linebreak</li>` ]
 **/
const resultDisplayArray = makeList(result.failure);