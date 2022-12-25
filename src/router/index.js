// import Vue from "vue";
import { createRouter, createWebHistory } from "vue-router";
import AlertVue from "./../components/AlertVue.vue";
import SignupEmployee from "./../components/SignupEmployee.vue";
import SignupEmployer from "./../components/SignupEmployer.vue";
import LoginEmployee from "./../components/LoginEmployee.vue";
import LoginEmployer from "./../components/LoginEmployer.vue";

const routes = [
    { path: "/", component: AlertVue },
    {
        path: "/employee",
        children: [
            { path: "signup", component: SignupEmployee },
            { path: "login", component: LoginEmployee },
        ],
    },
    {
        path: "/employer",
        children: [
            { path: "signup", component: SignupEmployer },
            { path: "login", component: LoginEmployer },
        ],
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
