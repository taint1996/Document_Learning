const iceCreams = [{
    flavor: 'pineapple',
    color: 'white'
},
{
    flavor: 'strawberry',
    color: 'red'
},
{
    flavor: 'watermelon',
    color: 'red'
},
{
    flavor: 'kiwi',
    color: 'green'
},
{
    flavor: 'mango',
    color: 'yellow'
},
{
    flavor: 'pear',
    color: 'green'
}
];

const getRed = iceCreams.filter(i => i.color === "red");

const getFlavours = iceCreams.map(i => i.flavor);

const flavours = [
    "strawberry",
    "strawberry",
    "kiwi",
    "kiwi",
    "kiwi",
    "strawberry",
    "mango",
    "kiwi",
    "banana"
];
////// output:  
// {
//     strawberry: 3,
//     kiwi: 4,
//     mango: 1, 
//     banana: 1 
// }

const amountFlavours = flavours.reduce((acc, curr) => {
    acc[curr] = acc[curr] ? (acc[curr] + 1) : (acc[curr] = 1)
    return {
        ...acc,
        curr: acc[curr]
    }
}, {});


const getColor = iceCreams.map(i => i.color);

const amountColors = getColor.reduce((colors, color) => {
    let amount = colors[color] ? (colors[color] + 1) : (colors[color] = 1);
    return {
        ...colors,
        color: amount
    }
}, {});
console.log(amountColors);