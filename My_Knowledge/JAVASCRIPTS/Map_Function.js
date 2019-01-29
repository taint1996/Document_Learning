// Examples 2: Given this javascript array of objects:
const songs = [
    { id: 1, name: "Curr of the Burl", artist: "Mastodon"}, 
    { id: 2, name: "Oblivion", artist: "Mastodon"}, 
    { id: 3, name: "Flying Whales", artist: "Gojira"}, 
    { id: 4, name: "L'Envast Sauvage", artist: "Gojira"}
];

const allSongNames = songs.map(i => i.name);
// console.log(allSongNames);

const allSongNameLowercase = songs.map(i => i.name.toLowerCase());

const lowercaseSongNameFunction = song => {
    return song.name.toLowerCase();
}
const lowerCasesong = songs.map(lowercaseSongNameFunction);
// console.log(lowerCasesong);

//////////////// Example 3: Divisible by 3
const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];

const divisibleByThrreeES5 = array.filter(function (v){
    return v % 3 === 0;
});
// console.log("Divisible 3 ES5:", divisibleByThrreeES5);

const divisibleByThrreeES6 = array.filter(v => v % 3 === 0);
// console.log("Divisible 3 ES6:", divisibleByThrreeES6);

// Max number Array
const isMaxNumber = array.reduce((a, b) => { return Math.max(a,b)} );

const sumArray = array.reduce((accumulator, currentValue) => accumulator + currentValue , 0);

// Challenge 1
    // input = [{ name: "abc"}, {name: "xyz"}];
    // output = ['abc', 'xyz'];

const input = [{ name: "abc"}, {name: "xyz"}];
const output = input.map(i => i.name);
console.log(output);

const newInput = output.reduce((acc, curr) => {
    acc[curr] = curr;
    return acc;
} , {});
console.log(newInput);