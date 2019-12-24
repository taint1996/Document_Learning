var myObj = new Vue({
  el: '#app-4',
  data: {
    todos: [
      { text: "Learn Javascript" },
      { text: "Learn Vue" },
      { text: "Build something awesome" }
    ]
  }
});

myObj.todos.push({ text: "Making simple "});