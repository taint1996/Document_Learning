// Các đối tượng có thể được coi là lưu trữ khóa / giá trị, giống như một từ điển. Nếu bạn có dữ liệu dạng bảng, 
    // bạn có thể sử dụng một đối tượng để "lookup" các giá trị thay vì một câu lệnh chuyển đổi hoặc chuỗi if / else
    // Điều này hữu ích nhất khi bạn biết rằng dữ liệu đầu vào của bạn bị giới hạn trong một phạm vi nhất định.

// Setup
function phoneticLookup(val) {
    var result = "";
    // Only change code below this line  
    var lookup = {
        "alpha": "Adams",
        "bravo": "Boston",
        "charlie": "Chicago",
        "delta": "Denver",
        "echo": "Easy",
        "foxtrot": "Frank"
    };
    result = lookup[val];
    // Only change code above this line
    return result;
}

// Change this value to test
phoneticLookup("alpha")
phoneticLookup("bravo")
phoneticLookup("charlie");
phoneticLookup("delta");
phoneticLookup("echo");
phoneticLookup("foxtrot");
phoneticLookup("");

// Testing Objects for Properties: use .hasOwnProperty() return true false if property is found or not
var myObj = {
    gift: "pony",
    pet: "kitten",
    bed: "sleigh"
};

function checkObj(checkProp) {
    // Your Code Here
    if (myObj.hasOwnProperty(checkProp)) {
        return myObj[checkProp];
    } else {
        return "Not Found";
    }
}

// Test your code by modifying these values
checkObj("gift");
checkObj("pet");
checkObj("house");
