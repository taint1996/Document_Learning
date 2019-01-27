// Write a JavaScript function to find the area of a triangle where lengths of the three of its sides are 5, 6, 7.
const sideA = 5;
const sideB = 6;
const sideC = 7;

const S = (sideA + sideB + sideC) / 2; // chu vi

const area = Math.sqrt(S * (S - sideA) * (S - sideB) * (S - sideC)); // dien tich
console.log("Area Triangle: ", area);
