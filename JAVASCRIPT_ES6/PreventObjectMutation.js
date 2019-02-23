// As seen in the previous challenge, 
    // const declaration alone doesn't really protect your data from mutation. 
    // To ensure your data doesn't change, JavaScript provides a function Object.freeze to prevent data mutation.
// Once the object is frozen, you can no longer add, update, or delete properties from it. 
    // Any attempt at changing the object will be rejected without an error.
function freezeObj() {
    "use strict";
    const MATH_CONSTANTS = {
        PI: 3.14
    };
    // change code below this line
    Object.freeze(MATH_CONSTANTS);
    
    // change code above this line
    try {
        MATH_CONSTANTS.PI = 99;
    } catch( ex ) {
        console.log(ex);
    }
    return MATH_CONSTANTS.PI;
    }
    const PI = freezeObj();