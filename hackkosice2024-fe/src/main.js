import { createApp } from "vue";
import App from "./App.vue";
import PrimeVue from "primevue/config";
import axios from "axios";
import VueAxios from "vue-axios";

import "primevue/resources/themes/aura-light-green/theme.css";
import "./index.scss";

const app = createApp(App);

app.use(PrimeVue);
app.use(VueAxios, axios);

app.mount("#app");
