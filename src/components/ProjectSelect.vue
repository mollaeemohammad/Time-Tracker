<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useInitData } from "../composables/initData";
import { useUserStore } from "../stores/user";

const store = useUserStore();
const router = useRouter();
const projects = ref([]);

async function setProjects(token) {
    const response = await axios({
        method: "get",
        url: "api/get_projects_of_employer",
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });

    if (!response.data.status) {
        projects.value = response.data;
    }
}

function selectProject(projectInfo) {
    console.log(projectInfo);
    const currentProjectObj = {
        name: projectInfo[0],
        description: projectInfo[1],
        status: "Unfinished",
    };
    localStorage.setItem("employer_project", JSON.stringify(currentProjectObj));
    router.push({ name: "homeEmployer" });
}

async function removeProject(projectInfo) {
    const response = await axios.post(
        "api/delete_project",
        {
            project_name: projectInfo[0],
        },
        { headers: { Authorization: `Bearer ${store.token}` } }
    );
    console.log(response);

    if (!(response.data.status < 400 || response.data.message === "Successful"))
        return;

    const empIndex = projects.value.findIndex(
        (proj) => proj[0] === projectInfo[0]
    );
    projects.value.splice(empIndex, 1);
}

onMounted(() => {
    useInitData();
    setProjects(store.token);
});
</script>

<template>
    <v-app>
        <v-app-bar>
            <template v-slot:prepend>
                <v-btn
                    icon="mdi-chevron-left"
                    size="large"
                    class="text-h6"
                    to="home"
                ></v-btn>
            </template>

            <v-app-bar-title>Select project</v-app-bar-title>
        </v-app-bar>
        <v-main>
            <v-container max-width="800">
                <v-btn
                    color="success"
                    block
                    size="90"
                    @click="router.push({ name: 'projectEmployer' })"
                >
                    <v-icon size="40">mdi-plus</v-icon>
                    <p class="mx-3">add new project</p>
                </v-btn>

                <v-hover
                    v-slot="{ isHovering, props }"
                    v-for="project in projects"
                >
                    <v-card
                        class="mx-auto my-8 pa-5"
                        :class="{ 'on-hover-cursor': isHovering }"
                        :color="isHovering ? 'indigo-lighten-4' : ''"
                        v-bind="props"
                    >
                        <v-card-text @click="selectProject(project)">
                            <v-row class="text-center" align="center">
                                <v-col
                                    cols="5"
                                    class="text-h5 text-light-blue-darken-4"
                                >
                                    <p>{{ project[0] }}</p>
                                </v-col>
                                <v-col cols="5">
                                    <p>Unfinished</p>
                                </v-col>
                                <v-col cols="1">
                                    <v-btn
                                        icon
                                        color="info"
                                        @click="
                                            router.push({
                                                name: 'projectEmployer',
                                                params: {
                                                    projectName: project[0],
                                                },
                                            })
                                        "
                                    >
                                        <v-icon>mdi-pencil</v-icon>
                                    </v-btn>
                                </v-col>
                                <v-col cols="1">
                                    <v-btn
                                        icon
                                        color="error"
                                        @click="removeProject(project)"
                                    >
                                        <v-icon>mdi-delete</v-icon>
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-card-text>
                    </v-card>
                </v-hover>
            </v-container>
        </v-main>
    </v-app>
</template>

<style>
.on-hover-cursor {
    cursor: pointer;
}
</style>
