<script setup>
import { onMounted, onUnmounted, ref } from "vue";
import { useRouter } from "vue-router";
import { useInitData } from "../composables/initData";
import { useUserStore } from "../stores/user";

const store = useUserStore();
const router = useRouter();
const role = useInitData();
const currentProjectName = store.currentProject.name;
const currentProjectStatus = store.currentProject.status;
const currentTime = ref("");
const isProjectExist = ref(false);

let updateTimeHandler;

const setCurrentTime = function () {
    const today = new Date();
    const calcTime =
        today.getHours().toString().padStart(2, "0") +
        ":" +
        today.getMinutes().toString().padStart(2, "0");
    currentTime.value = calcTime;
};

onMounted(() => {
    setCurrentTime();
    if (role !== "employer") router.push({ name: "login" });
    updateTimeHandler = setInterval(setCurrentTime, 1000 * 20);
});

onUnmounted(() => {
    clearInterval(updateTimeHandler);
});

if (!role) router.push("/login");
</script>

<template>
    <v-app>
        <v-main>
            <div class="text-center my-8">
                <h2 class="text-h5">Welcome, {{ store.username }}</h2>
            </div>
            <div class="text-center py-4">
                <h2 class="text-h2 mb-2">{{ currentTime }}</h2>
                <h3 class="text-subtitle-1">Friday, 6 January</h3>
            </div>

            <v-row justify="center" class="my-5">
                <v-btn
                    color="info"
                    size="175"
                    icon
                    @click="router.push({ name: 'selectProjectEmployer' })"
                >
                    <div class="pa-1">
                        <p>select</p>
                        <p>project</p>
                    </div>
                    <v-icon size="50" right>mdi-gesture-tap</v-icon>
                </v-btn>
            </v-row>

            <v-card class="mx-auto" width="80%" rounded>
                <v-card-item>
                    <v-container>
                        <v-row align="center" class="text-center">
                            <v-col cols="8"
                                ><div class="text-h4 text-light-blue-darken-4">
                                    <span>{{
                                        currentProjectName || "----"
                                    }}</span>
                                </div></v-col
                            >
                            <v-col cols="4"
                                ><div>
                                    <span>status:</span
                                    ><span class="mx-3">{{
                                        currentProjectStatus || "--"
                                    }}</span>
                                </div>
                            </v-col>
                        </v-row>
                        <v-divider class="w-75 mt-5 mx-auto"></v-divider>
                    </v-container>
                </v-card-item>
                <v-card-item class="text-center">
                    <!-- <v-sheet elevation="3" class="ma-5 pa-5">
                        <v-row>
                            <v-col cols="6" class="text-h6"
                                >Empolyee Name: --
                            </v-col>
                            <v-col cols="3">Payment: --</v-col>
                            <v-col cols="3">Hours: --</v-col>
                        </v-row>
                    </v-sheet> -->
                    <div v-if="!isProjectExist">
                        <v-icon size="75"
                            >mdi-account-multiple-plus-outline
                        </v-icon>
                        <p class="text-h6">Add project to see employers</p>
                    </div>
                </v-card-item>
            </v-card>
        </v-main>
    </v-app>
</template>
