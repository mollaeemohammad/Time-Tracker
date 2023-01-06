// import Vue from "vue";
import { createRouter, createWebHistory } from "vue-router";
import AlertVue from "./../components/AlertVue.vue";
import SignupForm from "./../components/signupForm.vue";
import LoginForm from "./../components/loginForm.vue";
import HomeEmployer from "./../components/HomeEmployer.vue";
import ProjectRegister from "./../components/ProjectRegister.vue";
import Test from "./../components/Test.vue";
import Test2 from "./../components/Test2.vue";
import Test3 from "./../components/Test3.vue";

const routes = [
    { path: "/", component: AlertVue },
    { path: "/signup", name: "signup", component: SignupForm },
    { path: "/login", name: "login", component: LoginForm },
    {
        path: "/home",
        name: "home",
        component: HomeEmployer,
        children: [],
    },
    {
        path: "/project",
        name: "home-project",
        component: ProjectRegister,
    },

    { path: "/test", name: "test", component: Test },
    {
        path: "/test2",
        name: "test2",
        component: Test2,
    },
    { path: "/test3", name: "test3", component: Test3 },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
