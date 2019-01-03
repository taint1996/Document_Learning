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

