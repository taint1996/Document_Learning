// Accessing Object Properties with Dot Notation
var testObj = {
    "hat": "ballcap",
    "shirt": "jersey",
    "shoes": "cleats"
};

var hatValue = testObj.hat;
var shirtValue = testObj.shirt;
var shoesValue = testObj.shoes;

// Accessing Object Properties with Bracket Notation : Cách thứ hai để truy cập các thuộc tính của một đối tượng là ký hiệu ngoặc ([]). 
    // Nếu thuộc tính của đối tượng bạn đang cố truy cập có một khoảng trắng trong tên của nó bạn sẽ cần sử dụng ký hiệu ngoặc.
var myObj = {
    "Space Name": "Kirk",
    "More Space": "Spock",
    "NoSpace": "USS Enterprise"
};
myObj["Space Name"]; // Kirk
myObj['More Space']; // Spock
myObj["NoSpace"]; // USS Enterprise

var testObjBracket = {
    "an entree": "hamburger",
    "my side": "veggies",
    "the drink": "water"
};
var entreeValue = testObjBracket["an entree"];
var mySideValue = testObjBracket["my side"];
var theDrinkValue = testObjBracket["the drink"];

// Accessing Object Properties with Variables: Truy cập các thuộc tính đối tượng với các biến
    // Một cách sử dụng ký hiệu ngoặc khác trên các đối tượng là truy cập vào một thuộc tính được lưu trữ dưới dạng giá trị của một biến. 
    // Điều này có thể rất hữu ích để lặp qua các thuộc tính của đối tượng hoặc khi truy cập bảng tra cứu.
var playerName = {
    12: "Namath",
    16: "Montana",
    19: "Unitas"
};

var playerNumber = 16;
var player = playerName[playerNumber];

////// After you've created a JavaScript object, you can update its properties at any time just like you would update any other variable. 
    ////// You can use either dot or bracket notation to update.
var ourDog = {
    "name": "Camper",
    "legs": 4,
    "tails": 1,
    "friends": ["everything!"]
};

ourDog.bark = "bow-wow";

// Setup
var myDog = {
"name": "Happy Coder",
"legs": 4,
"tails": 1,
"friends": ["freeCodeCamp Campers"]
};

myDog.bark = "wolf";
console.log(myDog)

////// Delete Properties from a JavaScript Object
delete myDog.tails;
