/// Using .reduce()
var pilots = [ 
  { 
    id: 10, 
    name: "Poe Dameron",  
    years: 14, 
  }, 
  { 
    id: 2, 
    name: "Temmin 'Snap' Wexley",  
    years: 30, 
  }, 
  { 
    id: 41, 
    name: "Tallissan Lintra",  
    years: 16, 
  }, 
  { 
    id: 99, 
    name: "Ello Asty",  
    years: 22, 
  } 
];

var totalYears = pilots.reduce(function(accumulator, pilot){
  return accumulator + pilot.years;
}, 0);


// using in Babel or TypeScript
const totalYears = pilots.reduce((acc, pilot) => acc + pilot.years, 0);

var mostExpPilot = pilots.reduce(function (oldest, pilot) {
  return (oldest.years || 0) > pilot.years ? oldest : pilot;
}, {});

////////////////// Example
var epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
const reduceEpicWords = epic.reduce((acc, curr) => acc + " " + curr);
console.log("reduceEpicWords: ", reduceEpicWords);

////////////////// Example: 
// Output = { 'George Washington': 'george@us.gov',
//   'John Adams': 'john@us.gov',
//   'Thomas Jefferson': 'thomas@us.gov',
//   'James Madison': 'james@us.gov' }

var users = [{ fullName: 'George Washington', email: 'george@us.gov' },
             { fullName: 'John Adams', email: 'john@us.gov' },
             { fullName: 'Thomas Jefferson', email: 'thomas@us.gov' },
             { fullName: 'James Madison', email: 'james@us.gov' }];
const infoUser = users.reduce((acc, curr) => { acc[curr.fullName] = curr.email;
  return acc[curr.fullName] }, {});

