// A more practical reduce() example
/* Let’s do something a bit more useful with our reduce() method. 
   Let’s calculate the results of a vote for the best ice cream flavor */
const flavours = [
    "strawberry",
    "strawberry",
    "kiwi",
    "kiwi",
    "kiwi",
    "strawberry",
    "mango",
    "kiwi",
    "banana"
];

const amountFlavours = flavours.reduce((acc, curr) => ({
    ...acc, 
    curr: (!acc[curr]) ? (acc[curr] = 1) : (acc[curr]++)
}), {});
console.log("Amount Flavours: ", amountFlavours);

const votesFlavours = (votes, vote) => {
    votes[vote] = !votes[vote] ? (votes[vote] = 1) : (votes[vote] + 1);
    return votes;
}
const amountFlavours2 = flavours.reduce(votesFlavours, {});
console.log("amount Flavours", amountFlavours2);
console.log("Strawberry: ", amountFlavours2.strawberry);
console.log("Kiwi: ", amountFlavours2.kiwi);
console.log("Mango: ", amountFlavours2.mango);
console.log("Banana: ", amountFlavours2.banana);