function greeter(person) {
    return "Hello " + person.firstName + " " + person.lastName;
}
var user = { firstName: "Tai", lastName: "Beo Kun" };
document.body.innerHTML = greeter(user);
