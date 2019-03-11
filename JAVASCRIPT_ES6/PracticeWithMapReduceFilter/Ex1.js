const officers = [{
        id: 20,
        name: 'Captain Piett'
    },
    {
        id: 24,
        name: 'General Veers'
    },
    {
        id: 56,
        name: 'Admiral Ozzel'
    },
    {
        id: 88,
        name: 'Commander Jerjerrod'
    }
];

const officerIds = officers.map(i => i.id);

// reduce 
const pilots = [{
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

const totalYears = pilots.reduce((acc, curr) => acc += curr.years, 0);
const mostExpPilot = pilots.reduce((oldest, pilot) => {
    return (oldest.years || 0) > pilot.years ? oldest : pilot
}, {});
console.log("most Experience Pilot", mostExpPilot);

// filter 
const factions = [
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
const isEmpire = (i => i.faction === "Empire");
const getEmpire = factions.filter(isEmpire);
console.log("getEmpire", getEmpire);

const isRebel = (i => i.faction === "Rebels");
const getRebel = factions.filter(isRebel);
console.log("getRebel", getRebel);

const insertYearstoFactions = { ...factions, years: pilots.years };
console.log(insertYearstoFactions);