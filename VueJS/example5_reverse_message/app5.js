var app5 = new Vue({
  el: '#app-5',
  data: {
    message: 'Hello Vue.js'
  },
  methods: {
    reverseMsg: function() {
      this.message = this.message.split('').reverse().join('');
    }
  },
});