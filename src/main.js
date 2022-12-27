import { createApp } from "vue";
import vuetify from "./plugins/vuetify";
import "./style.css";
import App from "./App.vue";
import "./axios";
import router from "./router/index";

const app = createApp(App);
app.use(router);
app.use(vuetify);
app.mount("#app");
