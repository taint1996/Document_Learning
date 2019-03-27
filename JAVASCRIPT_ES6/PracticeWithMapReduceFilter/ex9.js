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