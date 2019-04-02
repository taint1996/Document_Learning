class User {
	constructor(name, age, email) {
		this._name = name;
		this._age = age;
		this._email = email;
	}

	get name() {
		return this._name;
	}

	set name(newName) {
		this._name = newName;
	}
}

class Adminstrator extends User {
	construtor(name, age, email, role) {
		super(name, age, email)
		this._role = role;
	}

	get role() {
		return _role;
	}

	set role(newRole) {
		this._role = newRole;
	}
}

const beoka = new Adminstrator("Tai Beo", 23, "taibeoka1996@gmail.com", "Admin");
console.log(beoka.name);
console.log(beoka.role);