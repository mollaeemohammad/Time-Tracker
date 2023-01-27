<script setup>
import axios from "axios";
import { ref, reactive, computed, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import { useInitData } from "../composables/initData";
import { useUserStore } from "../stores/user";
import LineChart from "./LineChart.vue";

const store = useUserStore();
const router = useRouter();
const projectsList = ref([]);
const selectedProject = ref("");

async function setProjects(token) {
    const response = await axios({
        method: "get",
        url: "api/get_projects_of_employee",
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });

    console.log(response);

    if (!response.data.status) {
        projectsList.value = response.data.map((data) => data[0]);
        selectedProject.value = projectsList.value[0] || "";
    }
}

onMounted(() => {
    useInitData();
    // if (store.role !== "employee") router.push({ name: "login" });
    setProjects(store.token);
});
</script>

<template>
    <v-app style="height: 90vh">
        <v-main>
            <div class="my-6 mx-auto w-25">
                <v-select v-model="selectedProject" :items="projectsList">
                </v-select>
            </div>
            <v-container
                class="mt-16"
                style="max-width: 800px; background-color: rgba(5, 14, 16, 0.9)"
            >
                <LineChart :chart-data="[7, 2.9, 12, 10, 4.5, 8, 7]" />
            </v-container>
        </v-main>
    </v-app>
</template>
