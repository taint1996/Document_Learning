// 20 String Methods
var stringOne = "freeCodeCamp is the best place to learn";
var stringTwo = "frontend and backend development";

// charAt()
console.log(`Char At(1) of ${stringOne} is ${stringOne.charAt(1)}`); // -> "r"

// charCodeAt()
console.log(`Char Code At(1) of ${stringOne} is ${stringOne.charCodeAt(1)}`); // -> r: 114

// concat(): combine stringTwo into stringOne (stringOne + stringTwo)
console.log(`Concat: ${stringOne.concat(stringTwo)}`);

// endsWith("to"): check string is end with word to?
console.log("End With String by \"to\"???", stringOne.endsWith("to")); // -> false

// fromCharCode(114): 114 return to "r", 65 return to A
console.log("From Char Code:", String.fromCharCode(114));
console.log("From Char Code:", String.fromCharCode(65)); // => A

// includes() -> check word that is in a string 
console.log("Is this include end word?", stringTwo.includes("end"));

// indexOf() will return first found occurence of a specified value in a string
console.log("Index of stringTwo is", stringTwo.indexOf("end")); // -> 5
// lastIndexOf() will return last found occurence of a specified value in a string
console.log("Index of stringTwo is", stringTwo.lastIndexOf("end")); // -> 17

// match() Regular Expression : return an array containing the results of that search
console.log(stringTwo.match(/end/g)); // -> ["end", "end"]

// repeat(): will return a string value, stringOne use repeat will repeat n times when u used it
console.log(stringOne.repeat(3));

// replace() (Regular Expression): will replace a -> b
console.log(`Replace String One: ${stringTwo.replace(/end/g, "END")}`);

// search(): Finds the first substring match in a regular expression search.
console.log(stringTwo.search("end")); // -> position 5

// slice() Returns a section of a string.
console.log(stringTwo.slice(2,4)); // -> "on"

// split() Split a string into substrings using the specified separator and return them as an array.
console.log(stringOne.split(" ")); // -> ["freeCodeCamp", "is", "the", "best", "place", "to", "learn"]

// startsWith(): check searchString is in position
console.log(stringOne.startsWith("on", 1)); // -> false
console.log(stringTwo.startsWith("on", 2)); // -> true

// substr(): Gets a substring beginning at the specified location and having the specified length
console.log(stringOne.substr(4, 4)); // -> "Code"

// substring(): Returns the substring at the specified location within a String object.
console.log(stringOne.substring(1, 8)); // -> "reeCodeCamp is the best place to learn", "reeCode"

// toLowerCase() -> return lowercase string
console.log("To Lower Case: ", stringOne.toLowerCase());

// toLowerCase() -> return UPPERCASE string
console.log("To UPPERCASE: ", stringOne.toUpperCase());

// trim(): Removes the leading and trailing white space and line terminator characters from a string.
const stringThree = "   Call Me Béo Ka";
console.log(stringThree.trim());