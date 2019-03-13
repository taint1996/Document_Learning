const user = {name: 'Shivek Khurana'};
const addUserInfo = {age: 23, email: "abc@gmail.com", password: "1234", ...user};
console.log(addUserInfo);

const deletePassordFromUser = (({name, age}) => ({ name, age}))(addUserInfo);
console.log(deletePassordFromUser);

const removePasswordFromUser = Object.keys(addUserInfo).reduce((acc, key) => 
    (key === "password") ? acc : ({ ...acc, [key]: addUserInfo[key] })
    // console.log(key)
, {});
console.log(removePasswordFromUser)

// Adding a key value pair with dynamic key
const dynamicKey = "wearSpectecles";
const updateUser = { ...user, [dynamicKey]: true};
console.log(updateUser);