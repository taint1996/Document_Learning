const users = [
    { id: 11, name: 'Adam', age: 23, group: 'editor' },
    { id: 47, name: 'John', age: 28, group: 'admin' },
    { id: 85, name: 'William', age: 34, group: 'editor' },
    { id: 97, name: 'Oliver', age: 28, group: 'admin' }
];

// Find and replace a key-value pair in an array of objects
const u = users.reduce((acc, curr) => ({
    ...acc,
    [curr.id]: curr
}), {});

const updatedUsers = users.map(i => i.id !== 47 ? i : {
    ...i,
    age: i.age + 1
});

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

// Create an array of Fahrenheit values from an array of Celsius values
const celsius = [-15, -5, 0, 10, 16, 20, 24, 32]
const fahrenheit = celsius.map(i => i * 1.8 + 32);
console.log(fahrenheit);

const params = {
    lat: 45,
    lng: 6,
    alt: 1000
};
// queryString is "lat=45&lng=6&alt=1000"
const queryString = Object.entries(params).map(p => encodeURIComponent(p[0]) + '=' + encodeURIComponent(p[1])).join('&');
console.log(queryString);