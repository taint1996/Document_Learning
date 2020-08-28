<template>
  <div class="home">
    <img src="@/assets/logo.png" id="vue-logo" width="100" height="100" />
    <div>What do i need to do today?</div>
    <input v-model="inpTodo" />
    <button @click="addTodo"></button>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data() {
    return {
      inpTodo: ""
    }
  },
  methods: {
    addTodo: function() {
      console.log(" myTodo: ", inpTodo);
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
}

body, html, #app {
  background: #8ac8e5;
}

.home {
  width: 300px;
  margin: 0 auto;
}

input, button {
  border: 0;
  width: 100%;
  margin: 0 0 10px;
  padding: 7px;
}

input {
  font-size: 12px;
}

button {
  background: #43b823;
  border: 0;
  text-transform: capitalize;
  color: #fff;
  font-weight: 700;
  cursor: pointer
}

.title {
  font-size: 14px;
  font-weight: 700;
  padding 0px 0p 10px 0px;
  border-bottom: 1px solid #666;
}

#errors {
  background: #a52222;
  color: #fff;
  padding: 50px;
}
</style>
