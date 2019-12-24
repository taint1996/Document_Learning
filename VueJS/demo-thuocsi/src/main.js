import Vue from "vue";
import BootstrapVue from "bootstrap-vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.use(BootstrapVue);

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faCoffee,
  faSpinner,
  faEdit,
  faCircle,
  faCheck,
  faPlus,
  faEquals,
  faArrowRight,
  faPencilAlt,
  faComment
} from "@fortawesome/free-solid-svg-icons";

import brands from "@fortawesome/fontawesome-free-brands";
import solid from "@fortawesome/fontawesome-free-solid";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
library.add(
  faCoffee,
  faSpinner,
  faEdit,
  faCircle,
  faCheck,
  faPlus,
  faEquals,
  faArrowRight,
  faPencilAlt,
  faComment,
  brands,
  solid
);
Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
