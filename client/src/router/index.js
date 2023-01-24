import Vue from "vue";
import VueRouter from "vue-router";
import AlertVue from "./../components/AlertVue";
import SignupEmployee from "./../components/SignupEmployee";
import SignupEmployer from "./../components/SignupEmployer";
import LoginEmployee from "./../components/LoginEmployee";
import LoginEmployer from "./../components/LoginEmployer";

Vue.use(VueRouter);

const routes = [
    { path: "/", component: AlertVue },
    { path: "/employee/signup", component: SignupEmployee },
    { path: "/employer/signup", component: SignupEmployer },
    { path: "/employee/login", component: LoginEmployee },
    { path: "/employer/login", component: LoginEmployer },
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router;
