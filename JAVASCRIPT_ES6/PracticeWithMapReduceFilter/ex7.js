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

const users = [
    { id: 11, name: 'Adam', age: 23, group: 'editor' },
    { id: 47, name: 'John', age: 28, group: 'admin' },
    { id: 85, name: 'William', age: 34, group: 'editor' },
    { id: 97, name: 'Oliver', age: 28, group: 'admin' }
];

const u = users.reduce((acc, curr) => ({
        ...acc,
        [curr.id]: curr }), {});
console.log(u);

const listOfUsersGroup = [...new Set(users.map(i => i.group))];
console.log(listOfUsersGroup);

const groupByAge = users.reduce((acc, curr) => {
    acc[curr.age] = acc[curr.age] + 1 || 1
    return acc;
}, {});
console.log(groupByAge);
// A simple search (case-sensitive)
const searchNameByFilter = users.filter(i => i.name.includes('oli'));
console.log(searchNameByFilter);

// A simple search (case-insensitive)
const searchNameInsentitive = users.filter(i => new RegExp('oli', 'i').test(i.name));
console.log(searchNameInsentitive);

//  Check if any of the users have admin rights
const hasAdmin = users.some(i => i.group.includes('admin'));

// flattening an array of integers
const nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
const flattenNested = nested.reduce((acc, curr) => [...acc, ...curr]);
console.log(flattenNested);

const flatNested = [].concat.apply([], nested);
console.log(flatNested);

const cities = {
    Lyon: 'France',
    Berlin: 'Germany',
    Paris: 'France'
};
// output {
//     France: ["Lyon", "Paris"],
//     Germany: ["Berlin"]
//   }

let countries = Object.keys(cities).reduce((acc, curr) => {
    let country = cities[curr];
    acc[country] = acc[country] || []    
    acc[country].push(curr);
    return acc;
}, {});
console.log(countries);


// Create an array of Fahrenheit values from an array of Celsius values
const celsius = [-15, -5, 0, 10, 16, 20, 24, 32]
const fahrenheit = celsius.map(i => i * 1.8 + 32);
console.log(fahrenheit);

const params = {lat: 45, lng: 6, alt: 1000};
// queryString is "lat=45&lng=6&alt=1000"
const queryString = Object.entries(params) .map(p => encodeURIComponent(p[0]) + '=' + encodeURIComponent(p[1])).join('&');
console.log(queryString);