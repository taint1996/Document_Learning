const updatedUsers = users.map(i => i.id !== 47 ? i : {...i, age: i.age + 1});
console.log(updatedUsers);

// Union (A ∪ B) of arrays
const arrA = [1, 4, 3, 2];
const arrB = [5, 2, 6, 7, 1];
const unionArray = [...new Set([...arrA, ...arrB])];
console.log(unionArray);

//  Intersection (A ∩ B) of arrays
const intersectionAB = arrA.filter(i => arrB.includes(i));
console.log(intersectionAB);