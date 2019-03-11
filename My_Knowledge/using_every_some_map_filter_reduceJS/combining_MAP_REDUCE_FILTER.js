var personal = [
	{
	id: 5, 
	  name: "Luke Skywalker",  
	  pilotingScore: 98,  
	  shootingScore: 56,  
	  isForceUser: true,  
	}, 
	{ 
	  id: 82, 
	  name: "Sabine Wren",  
	  pilotingScore: 73,  
	  shootingScore: 99,  
	  isForceUser: false,  
	}, 
	{ 
	  id: 22, 
	  name: "Zeb Orellios",  
	  pilotingScore: 20,  
	  shootingScore: 59,  
	  isForceUser: false,  
	}, 
	{ 
	  id: 15, 
	  name: "Ezra Bridger",  
	  pilotingScore: 43,  
	  shootingScore: 67,  
	  isForceUser: true,  
	}, 
	{ 
	  id: 11, 
	  name: "Caleb Dume",  
	  pilotingScore: 71,  
	  shootingScore: 85,  
	  isForceUser: true
	}
];

// use filter to check isForceUser
var jediPersonal = personal.filter(function(person){
	return person.isForceUser;
});
alert(jediPersonal);

// use map to get total pilot & shooting score when jediPerson = true
var jediScores = jediPersonal.map(function(score){
	return score.pilotingScore + score.shootingScore;
})
alert(jediScores);

// using reduce to get total jediScore
var totalJediScore = jediScores.reduce(function(acc, score){
	return acc + score;
}, 0)
alert(totalJediScore);



// Combine filter map reduce
var totalJediScore = personal
	.filter(function(person){
		return person.isForceUser;
	})
	.map(function(jedi){
		return jedi.pilotingScore + jedi.shootingScore;
	})
	.reduce(function(acc, score){
		return acc + score;
	}, 0);

// Refactor combine code
const totalJediScore = personal
	.filter(person => person.isForceUser)
	.map(jedi => jedi.pilotingScore + jedi.shootingScore)
	.reduce((acc, score) => acc + score, 0);