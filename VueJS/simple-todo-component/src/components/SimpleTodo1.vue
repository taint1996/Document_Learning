<template>
  <div class="container">
    <h3>Simple todo 1 - Component</h3>
    <div class="section">
      <input class="add-todo col-8 offset-2" type="text" v-model="newTodo" @keyup.enter="addTodo()"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Main',
  data() {
    return {
      todos: [
        { title: 'Learn Vue', finished: true, editing: false },
        { title: 'Create a todo', finished: false, editing: false },
        { title: 'Never use Vue.js', finished: false, editing: false },
        { title: 'Create another project', finished: false, editing: false },
        { title: 'Get hired as Vue programmer', finished: false, editing: false },
        { title: 'Stop coding', finished: false, editing: false }
      ],
      newTodo: ''
    }
  },
  methods: {
    addTodo() {
      //this.todos.push({ title: this.newTodo, finished: false })
      this.$emit('addTodo', this.newTodo);
      this.newTodo = '';
    },
    removeTodo(index) {
      this.todos.splice(index, 1);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  i {
    padding: 0em 0.5em;
  }

  .container {
    div {
      width: 80;
      margin: 0 auto;
    }
  }

  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
