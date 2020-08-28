var vueInstance = new Vue({
  el: "#app",
  data: {
    title: "Áo thun nam thể thao vải Nỉ",
    url: "https://www.lazada.vn/products/ao-thun-nam-han-quoc-form-rong-in-hinh-pin-yeu-hay-tim-yeu-vai-day-min-mat-mem-mai-co-gian-tot-thoang-mat-i302800210-s484464940.html?spm=a2o4n.searchlist.list.20.77bb6e17s03geU&search=1",
    img_src: "https://vn-test-11.slatic.net/p/5f47bc936c1f2a1835bd265042907870.jpg_340x340q80.jpg_.webp",
    target: "_blank",
    price: 10000,
    checked: true
  },
  methods: {
    say: (text) => {
      return "Hello " + text;
    },

    methods: {
      formatPrice() {
        var number = this.price

        return new Intl.format("de-DE", { style: 'currency', curency: "EUR"}).format(number)
      }
    }
  }
})