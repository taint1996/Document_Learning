// Accessing Nested Objects: Truy cập các đối tượng lồng nhau
    // The sub-properties of objects can be accessed by chaining together the dot or bracket notation.
    var myStorage = {
        "car": {
            "inside": {
                "glove box": "maps",
                "passenger seat": "crumbs"
            },
            "outside": {
                "trunk": "jack"
            }
        }
    };
    
    var gloveBoxContents = myStorage.car.inside["glove box"];

// Access Nested Array: Truy cập mảng lồng nhau
    // Như chúng ta đã thấy trong các ví dụ trước, các đối tượng có thể chứa cả các đối tượng lồng nhau và các mảng lồng nhau. 
    // Tương tự như truy cập các đối tượng lồng nhau, ký hiệu khung Array có thể được nối kết để truy cập các mảng lồng nhau.
    
// Setup
var myPlants = [
    { 
        type: "flowers",
        list: [
            "rose",
            "tulip",
            "dandelion"
        ]
    }, 
    {
        type: "trees",
        list: [
            "fir",
            "pine",
            "birch"
            ]
    }
];

// Only change code below this line

var secondTree = myPlants[1].list[1]; // Change this line