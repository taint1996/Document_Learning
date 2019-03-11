const users = [{
        id: 1,
        name: "Jonathon Haley",
        username: "Monte.Weber2",
        email: "Daphne43@yahoo.com",
        phone: "1-563-675-1857",
        website: "carmela.net",
        password: "hashed_password"
    },
    {
        id: 2,
        name: "Dean John",
        username: "dd.1",
        email: "deno@google.com",
        phone: "1-123-543-1857",
        website: "dd.net",
        password: "Dean_hashed_password"
    }
];

const newUser = {
    id: 3,
    name: "Béo Ka Kun",
    username: "dd.1",
    email: "beoka@google.com",
    phone: "1-123-543-1857",
    website: "dd.net",
    password: "Dean_hashed_password"
};

// ARMD - Add, Read, Modify, Delete
// ARMD — Adding a new element to users
const atLastToUsers = [...users, newUser]; // at last to users
const atFirstToUsers = [newUser, ...users] // at first to users
const atNewUserByOldWay = users.concat(newUser);

// ARMD — Get email address, phone number and website of users into new array
const contactInfoUser = users.map(({email, phone, website}) => ({email, phone, website}));
console.log("contactInfoUser", contactInfoUser);

const reduceContactUser = users.reduce((acc, curr) => {
    const { email, phone, website } = curr;
    acc.push({ email, phone, website });
    return acc;
}, []);


// ARMD — Find and replace value for key of objects when id = 2
const start = Date.now()
const reduceToFindeUserWithIdIsTwo = users.reduce((acc, curr) => {
    (curr.id === 2) ? acc.push({...curr, name: "abc"}) : acc.push(curr);
}, []);
const end = Date.now();
const summary = (end - start) / 1000 + "secs"
console.log(findUserWithIdByTwo, summary);

// ARMD —Delete some key’s from object
const deleteWebsiteFromUsersByMap = users.map(({website, ...rest}) => rest);

const deleteWebsiteFromUsersByReduce = users.reduce((acc, curr) => {
    const deleteWebste = delete curr.website;
    acc.push(curr);
    return acc;
}, []);
