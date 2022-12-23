// import Vue from "vue";
import { createRouter, createWebHashHistory } from "vue-router";
import AlertVue from "./../components/AlertVue.vue";
import SignupEmployee from "./../components/SignupEmployee.vue";
import SignupEmployer from "./../components/SignupEmployer.vue";
import LoginEmployee from "./../components/LoginEmployee.vue";
import LoginEmployer from "./../components/LoginEmployer.vue";

// Vue.use(VueRouter);

const routes = [
    { path: "/", component: AlertVue },
    { path: "/employee/signup", component: SignupEmployee },
    { path: "/employer/signup", component: SignupEmployer },
    { path: "/employee/login", component: LoginEmployee },
    { path: "/employer/login", component: LoginEmployer },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
