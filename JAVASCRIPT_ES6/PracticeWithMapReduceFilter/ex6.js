//////////// 1
const arrayObj = [{ x: 1 }, { x: 2 }, { x: 3} ];
const sum = arrayObj.reduce((acc, curr) => acc + curr.x, 0);

//////////// 2: flatten array
const flattened = [[0, 1], [2, 3], [4, 5]].reduce((acc, curr) => acc.concat(curr), []);

//////////// amount loop name
const names = ['Alice', 'Bob', 'Tiff', 'Bruce', 'Alice'];
const amountName = names.reduce((acc, curr) => {
        let amount = acc[curr] ? (acc[curr] + 1) : (acc[curr] = 1);
        return {
            ...acc,
            curr: amount
        }
    }
, {})

//////////// group by object
const people = [
    { name: 'Alice', age: 21 },
    { name: 'Max', age: 20 },
    { name: 'Jane', age: 20 }
];
// groupedPeople is:
// { 
//   20: [
//     { name: 'Max', age: 20 }, 
//     { name: 'Jane', age: 20 }
//   ], 
//   21: [{ name: 'Alice', age: 21 }] 
// }

function groupBy(objectArray, property) {
    return objectArray.reduce(function (acc, obj) {
        var key = obj[property];
        if (!acc[key]) {
        acc[key] = [];
        }
        acc[key].push(obj);
        return acc;
    }, {});
}
console.log(groupBy(people, 'age'));
var groupedPeople = groupBy(people, 'age')


// const groupedPeople = people.reduce((acc, curr) => {
//     // let count;
//     // let amountAge = (acc[curr.age] === curr.age) ? (count + 1) : (count = 1)
//     // console.log();
//     // let amountAge = acc[curr.age] ? (acc[curr.age] + 1) : (acc[curr.age] = 1); 
//     // const arr = [];
//     // const output = {
//     //     ...acc[curr], 
//     //     [curr.age]: curr
//     // }
//     // const a = (amountAge) ? output : output
//     // console.log(a);

//     // console.log(amountAge);
//     // if (amountAge === 2) {
//     //     // const output = arr.push(curr);
//     //     const output = {
//     //         ...acc[curr], 
//     //         [curr.age]: curr
//     //     }   
        
                
//     //     console.log(output);
//     // }    
//     // else {
//     //     // return acc;
//     // }
//     // console.log(acc[amountAge]);

//     // return { 
//     //     ...acc,
//     //     curr: amountAge
//     //     // curr: amountAge 
//     // }
// }, {});
// console.log(groupedPeople);


