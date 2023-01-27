import { createApp } from "vue";
import { createPinia } from "pinia";
import vuetify from "./plugins/vuetify";
import "./style.css";
import App from "./App.vue";
import "./axios";
import router from "./router/index";

const app = createApp(App);
app.use(router);
app.use(createPinia());
app.use(vuetify);
app.mount("#app");
