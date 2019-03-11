const users = [{
        id: 1,
        name: "Jonathon Haley",
        username: "Monte.Weber2",
        email: "Daphne43@yahoo.com",
        phone: "1-563-675-1857 x11708",
        website: "carmela.net",
        password: "hashed_password"
    },
    {
        id: 2,
        name: "Dean John",
        username: "dd.1",
        email: "deno@google.com",
        phone: "1-123-543-1857 123212",
        website: "dd.net",
        password: "Dean_hashed_password"
    }
];

const newUser = {
    id: 3,
    name: "Béo Ka Kun",
    username: "dd.1",
    email: "beoka@google.com",
    phone: "1-123-543-1857 123212",
    website: "dd.net",
    password: "Dean_hashed_password"
};

const atLastToUsers = [...users, newUser]; // at last to users
const atFirstToUsers = [newUser, ...users] // at first to users
const atNewUserByOldWay = users.concat(newUser);

// ARMD — Get email address, phone number and website of users into new array
const contactInfoUser = users.map(({email, phone, website}) => ({email, phone, website}));
console.log("contactInfoUser", contactInfoUser);
