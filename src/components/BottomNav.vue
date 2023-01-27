<script setup>
import { ref, onMounted, onUpdated } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "../stores/user";

const router = useRouter();
const store = useUserStore();
const v = ref("home");

onMounted(() => {
    if (store.currentRouteName.startsWith("home")) {
        v.value = "home";
    } else if (store.currentRouteName.startsWith("profile")) {
        v.value = "profile";
    } else if (store.currentRouteName.startsWith("report")) {
        v.value = "report";
    }
});
</script>

<template>
    <v-app>
        <v-main>
            <router-view style="background-color: #0f2c33; color: #eee" />
            <!-- <router-view name="helper" /> -->
        </v-main>
        <v-bottom-navigation grow mode="shift" mandatory="true" v-model="v">
            <v-btn value="home" @click="router.push(v)">
                <v-icon>mdi-home</v-icon>

                <span>Home</span>
            </v-btn>

            <v-btn value="report" @click="router.push(v)">
                <v-icon>mdi-chart-line</v-icon>

                <span>Report</span>
            </v-btn>

            <v-btn value="notification">
                <v-icon>mdi-bell</v-icon>

                <span>Notifications</span>
            </v-btn>

            <v-btn value="profile" @click="router.push(v)">
                <v-icon>mdi-account</v-icon>

                <span>Profile</span>
            </v-btn>
        </v-bottom-navigation>
    </v-app>
</template>
