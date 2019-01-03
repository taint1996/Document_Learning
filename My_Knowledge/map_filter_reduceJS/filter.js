// Using .filter
var pilots = [ 
  { 
    id: 2, 
    name: "Wedge Antilles",  
    faction: "Rebels",  
  }, 
  { 
    id: 8, 
    name: "Ciena Ree", 
    faction: "Empire",  
  }, 
  { 
    id: 40, 
    name: "Iden Versio",  
    faction: "Empire",  
  }, 
  { 
    id: 66, 
    name: "Thane Kyrell",  
    faction: "Rebels",  
  } 
];

var rebels = pilots.filter(function (pilot) {  
  return pilot.faction === "Rebels";  
});

var empire = pilots.filter(function (pilot) {  
  return pilot.faction === "Empire";  
});

// #### even shorter with arrow functions
const rebels = pilots.filter(pilot => pilot.faction === "Rebels");

const empire = pilots.filter(pilot => pilot.faction === 'Empire');