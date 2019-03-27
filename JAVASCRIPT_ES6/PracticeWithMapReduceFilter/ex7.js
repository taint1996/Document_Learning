const values = [3, 1, 3, 5, 2, 4, 4, 4];
const uniqueValues = [...new Set(values)]

const uniqueValueByFilter = values.filter((v, i) => values.indexOf(v) === i);

const names = ['John', 'Paul', 'George', 'Ringo', 'John'];
const removeDuplicate = (names) => {
    let unique = {};

    names.forEach(i => {
        console.log(i);

        if (!unique[i]) {
            unique[i] = true;
        }
    })
    return Object.keys(unique);
}

const users = [{
        id: 11,
        name: 'Adam',
        age: 23,
        group: 'editor'
    },
    {
        id: 47,
        name: 'John',
        age: 28,
        group: 'admin'
    },
    {
        id: 85,
        name: 'William',
        age: 34,
        group: 'editor'
    },
    {
        id: 97,
        name: 'Oliver',
        age: 28,
        group: 'admin'
    }
];

// flattening an array of integers
const nested = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
const flattenNested = nested.reduce((acc, curr) => [...acc, ...curr]);
console.log(flattenNested);

const flatNested = [].concat.apply([], nested);
console.log(flatNested);