const companies = [
  { name: 'Company A', category: 'Finance', start: 1980, end: 2003 },
  { name: 'Company B', category: 'Retail', start: 1989, end: 2003 },
  { name: 'Company C', category: 'Auto', start: 1987, end: 2007 },
  { name: 'Company D', category: 'Technology', start: 1981, end: 2010 },
  { name: 'Company E', category: 'Finance', start: 2009, end: 2015 },
  { name: 'Company F', category: 'Auto', start: 2000, end: 2003 },
  { name: 'Company G', category: 'Technology', start: 2015, end: 2020 },
  { name: 'Company H', category: 'Retail', start: 1981, end: 1989 },
  { name: 'Company I', category: 'Auto', start: 2011, end: 2016 }
]

const ages = [33, 12, 20, 16, 5, 54, 21, 44, 61, 13, 15, 45, 25, 64, 32];

for(let i = 0; i < companies.length; i++) {
  console.log(companies[i]);
}

// forEach
// companies.forEach(function(company) {
//   console.log(company.name)
// })



let canDrinks = [];
for(let i = 0; i < ages.length; i++) {
  if (ages[i] >= 21) {
    canDrinks.push(ages[i])
  }
}

// filter age can drinks by filter
let canDrinksByFilter = ages.filter(age => age >= 21);
console.log(canDrinksByFilter)

// retail company by filter function
let retailsCompanies = companies.filter(function(company) {
  if (company.category === "Retail") {
    return true;
  }
})

// retail company by filter arrow function
let retailCompaniesES6 = companies.filter(company => company.category === "Retail")

// 80s Compannies
let eightiesCompanies = companies.filter(company => (company.start >= 1980 && company.start < 1990))

// Get companies the lastest 10 years or more
const latestTenYear = companies.filter(company => (company.end - company.start > 10))


// map
const companyNames = companies.map(company => {
  return `${company.name} working at ${company.start}-${company.end}`
})

const ageSquares = ages.map(age => Math.sqrt(age));
const multipleAges = ages.map(age => Math.pow(age, 2));

const ageMaps = ages.map(age => Math.sqrt(age))
                    .map(age => age * 2)



// sort
const sortedCompanies = companies.sort(function(c1, c2) {
  if (c1.start > c2.start) {
    return 1;
  } else {
    return -1;
  }
})

const sortedCompaniesES6 = companies.sort((comp1, comp2) => comp1.start > comp2.start ? 1 : -1)

const sortAges = ages.sort((age1, age2) => age1 - age2);

// reduce
const totalAges = ages.reduce((acc, curr) => acc + curr, 0);

// total years for all Companies
const totalYearCompanies = companies.reduce((total, company) =>  (total + (company.end - company.start)), 0)

// combined methods: age * 2 -> then filter age > 40 -> sort -> total age
const combinedAge = ages.map(age => age * 2)
                        .filter(age => age > 40)
                        .sort((minAge, maxAge) => minAge - maxAge)
                        .reduce((total, age) => total + age, 0);