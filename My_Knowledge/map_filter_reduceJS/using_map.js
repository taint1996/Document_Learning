var officers = [
	{id: 20, name: 'Captain Piett'},
	{id: 24, name: 'General Veers'},
	{id: 56, name: 'Admiral Ozzel'},
	{id: 88, name: 'Commander Jerjerrod'}	
]
// What we need: [20, 24, 56, 88]

//Using .forEach()
var officerIds = []
officers.forEach(function(officer){
	officerIds.push(officer.id);
});


// Using .map()
var officerIds = officers.map(function(officer){
	return officer.id;
});

#### require ES6 in Babel or TypeScript
const officerIds = officers.map(officer => officer.id)