// import Vue from "vue";
import { createRouter, createWebHistory } from "vue-router";
import AlertVue from "./../components/AlertVue.vue";
import SignupForm from "./../components/signupForm.vue";
import LoginForm from "./../components/loginForm.vue";
import HomeEmployer from "./../components/HomeEmployer.vue";
import HomeEmployee from "./../components/HomeEmployee.vue";
import ReportEmployee from "./../components/ReportEmployee.vue";
import ProfileEmployee from "./../components/ProfileEmployee.vue";
import ProjectRegister from "./../components/ProjectRegister.vue";
import ProjectSelect from "./../components/ProjectSelect.vue";
import BottomNav from "./../components/BottomNav.vue";
import Test from "./../components/Test.vue";
import Test2 from "./../components/Test2.vue";
import Test3 from "./../components/Test3.vue";
import Test4 from "./../components/Test4.vue";
import TestChart from "./../components/TestChart.vue";

const routes = [
    { path: "/", name: "main", component: AlertVue },
    { path: "/signup", name: "signup", component: SignupForm },
    { path: "/login", name: "login", component: LoginForm },

    { path: "/test", name: "test", component: Test },
    {
        path: "/app",
        name: "app",
        component: BottomNav,
        children: [
            {
                path: "employer/home",
                name: "homeEmployer",
                component: HomeEmployer,
            },
            {
                path: "employer/project/:projectName?",
                name: "projectEmployer",
                component: ProjectRegister,
            },
            {
                path: "employer/select",
                name: "selectProjectEmployer",
                component: ProjectSelect,
            },

            {
                path: "employer/profile",
                name: "profileEmployer",
                component: ProfileEmployee,
            },

            {
                path: "employee/home",
                name: "homeEmployee",
                component: HomeEmployee,
            },
            // {
            //     path: "employee/profile",
            //     name: "profileEmployee",
            //     component: ProfileEmployee,
            // },
            {
                path: "employee/profile",
                name: "profileEmployee",
                component: ProfileEmployee,
            },
            {
                path: "employee/report",
                name: "reportEmployee",
                component: ReportEmployee,
            },
            {
                path: "employer/report",
                name: "reportEmployer",
                component: ReportEmployee,
            },
        ],
    },
    { path: "/test3", name: "test3", component: Test3 },
    { path: "/chart", name: "chart", component: TestChart },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
