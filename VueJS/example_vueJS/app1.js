var myObject = new Vue({
  el: '#app-1',
  data: {
    message: "Hello VueJS!"
  }
});

function clickMe() {
  myObject.message = "My name is BeoKa"
}