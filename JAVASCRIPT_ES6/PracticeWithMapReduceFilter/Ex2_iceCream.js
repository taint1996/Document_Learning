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

const getFlavourRed = iceCreams.filter(i => i.color === "red")

const sameColor = (color) => { return iceCreams.filter(i => i.color === color) } ;
