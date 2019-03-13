const params = {color: 'red', minPrice: 8000, maxPrice: 10000};
// query is now "color=red&minPrice=8000&maxPrice=10000"

const paramsQuery = Object.keys(params).map(item => encodeURIComponent(item) + "=" + encodeURIComponent(params[item])).join("&");
console.log(paramsQuery)