//  Use Destructuring Assignment to Assign Variables from Nested Objects
const LOCAL_FORECAST = {
    today: { min: 72, max: 83 },
    tomorrow: { min: 73.3, max: 84.6 }
};

function getMaxOfTomorrow(forecast) {
    "use strict";

    const { tomorrow: { max: maxOfTomorrow } } = forecast;
    return maxOfTomorrow;
}

function getMinOfTomorrow(forecast) {
    "use strict";
    const { tomorrow: { min: minOfTomorrow }} = forecast;
    return minOfTomorrow;    
}

console.log(getMaxOfTomorrow(LOCAL_FORECAST));