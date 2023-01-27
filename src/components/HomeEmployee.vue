<script setup>
import axios from "axios";
import { ref, reactive, computed, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import { useInitData } from "../composables/initData";
import { useUserStore } from "../stores/user";

const store = useUserStore();
const router = useRouter();
const projectsList = ref([]);
const selectedProject = ref("");
const currentTime = ref("");
const workingState = ref("inactive");
const stateColor = ref("primary");
const stateIcon = ref("mdi-gesture-tap");
const workingTimes = reactive({
    checkIn: "",
    checkOut: "",
    lastPaused: "",
    workingHours: "",
});

let updateTimeHandler;

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

const setCurrentTime = function () {
    const today = new Date();
    const calcTime =
        today.getHours().toString().padStart(2, "0") +
        ":" +
        today.getMinutes().toString().padStart(2, "0");
    currentTime.value = calcTime;
};

const convertTimetoMin = function (timeValue) {
    if (!timeValue.includes(":")) return 0;
    const [hour, min] = timeValue.split(":");
    return +hour * 60 + +min;
};

const convertMinToTime = function (minNum) {
    const hour = Math.floor(minNum / 60);
    const min = minNum - hour * 60;
    return (
        hour.toString().padStart(2, "0") + ":" + min.toString().padStart(2, "0")
    );
};

const initWorkingState = function () {
    if (workingState.value === "inactive") {
        stateColor.value = "primary";
        stateIcon.value = "mdi-gesture-tap";
    } else if (workingState.value === "active") {
        stateColor.value = "success";
        stateIcon.value = "mdi-pause";
    } else if (workingState.value === "paused") {
        stateColor.value = "warning";
        stateIcon.value = "mdi-play";
    }
};

const setWorkingHours = function () {
    const lastPausedMin = convertTimetoMin(workingTimes.lastPaused);
    const currentMin = convertTimetoMin(currentTime.value);
    const workingMin = convertTimetoMin(workingTimes.workingHours);
    const diffMin = currentMin - lastPausedMin + workingMin;
    const diffTime = convertMinToTime(diffMin);
    workingTimes.workingHours = diffTime;
    workingTimes.lastPaused = currentTime.value;
};

async function insertWorkingHours() {
    const workingHour = convertTimetoMin(workingTimes.workingHours) / 60;
    console.log(workingHour);

    const response = await axios.post(
        `api/insert_hour`,
        {
            project_name: projectName.value,
            measured_hours: workingHour,
        },
        { headers: { Authorization: `Bearer ${token}` } }
    );
    console.log(response);

    if (
        !(response.data.status < 400 || response.data.message === "Successful")
    ) {
        // print error message
        return false;
    }
    return true;
}

const toggleWorkingState = function () {
    if (workingState.value === "inactive") {
        workingTimes.workingHours = "";
        workingTimes.checkIn = currentTime.value;
        workingTimes.lastPaused = currentTime.value;
    } else if (workingState.value === "active") {
        setWorkingHours();
    }

    if (workingState.value === "inactive" || workingState.value === "paused") {
        workingState.value = "active";
        stateColor.value = "success";
        stateIcon.value = "mdi-pause";
    } else if (workingState.value === "active") {
        workingState.value = "paused";
        stateColor.value = "warning";
        stateIcon.value = "mdi-play";
    }
};

const setInactiveWorkingState = async function () {
    workingState.value = "inactive";
    stateColor.value = "primary";
    stateIcon.value = "mdi-gesture-tap";
    setWorkingHours();
    workingTimes.checkOut = currentTime.value;
    // const DoesInserted = await insertWorkingHours();
};

onMounted(() => {
    useInitData();
    if (store.role !== "employee") router.push({ name: "login" });
    setCurrentTime();
    updateTimeHandler = setInterval(setCurrentTime, 1000 * 20);
    setProjects(store.token);
});

onUnmounted(() => {
    clearInterval(updateTimeHandler);
});
</script>

<template>
    <v-app style="height: 90vh">
        <v-main>
            <div class="my-6 mx-auto w-25">
                <v-select v-model="selectedProject" :items="projectsList">
                </v-select>
            </div>
            <div class="text-center pt-8">
                <h2 class="text-h2 mb-2">{{ currentTime }}</h2>
                <h3 class="text-subtitle-1">Friday, 6 January</h3>
            </div>

            <v-container class="text-center">
                <v-row justify="center">
                    <div style="position: relative">
                        <v-btn
                            :color="stateColor"
                            size="225"
                            class="my-5"
                            icon
                            @click="toggleWorkingState"
                        >
                            <v-icon size="50">{{ stateIcon }}</v-icon>
                        </v-btn>
                        <v-btn
                            v-show="workingState !== 'inactive'"
                            color="error"
                            size="60"
                            class="my-5"
                            icon
                            @click="setInactiveWorkingState"
                            style="position: absolute; bottom: 0; right: -100px"
                        >
                            <v-icon size="25">mdi-close</v-icon>
                        </v-btn>
                    </div>
                </v-row>
                <v-row justify="space-around">
                    <v-col>
                        <div><v-icon>mdi-clock-check-outline</v-icon></div>
                        <div>{{ workingTimes.checkIn || "--:--" }}</div>
                        <div class="text-caption">Check in</div>
                    </v-col>
                    <v-col>
                        <div><v-icon>mdi-clock-remove-outline</v-icon></div>
                        <div>{{ workingTimes.checkOut || "--:--" }}</div>
                        <div class="text-caption">Check out</div>
                    </v-col>
                    <v-col>
                        <div><v-icon>mdi-clock-plus-outline</v-icon></div>
                        <div>{{ workingTimes.workingHours || "--:--" }}</div>
                        <div class="text-caption">Working hours</div>
                    </v-col>
                </v-row>
                <v-row justify="center">
                    <div class="mt-5 text-h6">Total working hours: --:--</div>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>
