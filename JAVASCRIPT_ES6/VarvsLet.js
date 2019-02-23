/////////// Explore Differences Between the var and let Keywords: Khám phá sự khác biệt giữa var và let Keywords ///////////
// One of the biggest problems with declaring variables with the var keyword is that you can overwrite variable declarations without an error.
    // => Một trong những vấn đề lớn nhất khi khai báo biến với từ khóa var là bạn có thể ghi đè khai báo biến mà không gặp lỗi.

// One of the biggest problems with declaring variables with the var keyword is that you can overwrite variable declarations without an error.
//  Because this behavior does not throw an error, searching and fixing bugs becomes more difficult.
// A new keyword called let was introduced in ES6 to solve this potential issue with the var keyword.

// So unlike var, when using let, a variable with the same name can only be declared once.

// Note the "use strict". This enables Strict Mode, which catches common coding mistakes and "unsafe" actions. For instance:


let catName;
let quote;
function catTalk() {
    "use strict";

    catName = "Oliver";
    quote = catName + " says Meow!";
}
catTalk();


////////// Compare Scopes of the var and let Keywords: So sánh phạm vi từ khóa của var và let ///////////
// When you declare a variable with the var keyword, 
    // it is declared globally, or locally if declared inside a function: Khi bạn khai báo biến với keyword var, nó sẽ khai báo toàn cục hoặc cục bộ nếu khai báo bên trong function

///////// The let keyword behaves similarly, but with some extra features. 
    // When you declare a variable with the let keyword inside a block, statement, or expression, 
    // its scope is limited to that block, statement, or expression 
    // -> Khi bạn khai báo một biến với từ khóa let bên trong một khối, câu lệnh hoặc biểu thức, phạm vi của nó bị giới hạn trong khối, câu lệnh hoặc biểu thức đó.

/// Example let
'use strict';
let printNumTwo;
for (let i = 0; i < 3; i++) {
    if (i === 2) {
    printNumTwo = function() {
        return i;
    };
    }
}
console.log(printNumTwo());
// returns 2
console.log(i);
// returns "i is not defined"

// Example var
var numArray = [];
for (var i = 0; i < 3; i++) {
    numArray.push(i);
}
console.log(numArray);
// returns [0, 1, 2]
console.log(i);
// returns 3

