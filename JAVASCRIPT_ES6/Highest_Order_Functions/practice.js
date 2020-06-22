var carts = [
  {"name":"Biscuits", "type":"regular", "category":"food", "price": 2.0},
  {"name":"Monitor", "type":"prime", "category":"tech", "price": 119.99},
  {"name":"Mouse", "type":"prime", "category":"tech", "price": 25.50},
  {"name":"dress", "type":"regular", "category":"clothes", "price": 49.90},
]

// forEach
const eachCarts = carts.forEach((cart) => {
  console.log(`${cart.name} has price $${cart.price}`);
});

// map
const nameCarts = carts.map(cart => cart.name)
console.log(`name cart ${nameCarts.join(", ")}`)

const techCarts = carts.filter(cart => cart.category === "tech")

// filter
const primeCarts = carts.filter(cart => cart.type === "prime")
console.log(primeCarts);

const regularCarts = carts.filter(cart => cart.type === "regular");
console.log(regularCarts);

// reduce
const totalRegularPrices = carts.reduce((acc, curr) => {
  if (curr.type === "regular") {
    return acc + curr.price
  }
  return acc;
}, 0)
console.log(`Total regular prices: ${(totalRegularPrices)}`)

const totalPrimePrices = primeCarts.reduce((acc, curr) => acc + curr.price, 0);
console.log(`Total prime prices: ${Math.ceil(totalPrimePrices)}`);