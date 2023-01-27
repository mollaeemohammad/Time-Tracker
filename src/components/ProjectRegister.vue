<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useInitData } from "../composables/initData";
import { useUserStore } from "../stores/user";

const store = useUserStore();
const router = useRouter();
const route = useRoute();

const form = ref(null);
const empForm = ref(null);

const projectName = ref("");
const description = ref("");
const username = ref("");
const payment = ref(0);
const employeeList = ref([]);

const requiredRule = ref((v) => !!v || "This field is required");
const blankRule = ref((v) => (v && !!v.trim()) || "Value cannot be blank");
const namingRules = ref([requiredRule.value, blankRule.value]);
const positiveRule = ref((v) => v > 0 || "Value should be positive");

const employeeRepeatError = ref(false);
const formErrorState = ref(false);
const formErrorMessage = ref("");

const isEditing = ref(false);

function showEmployeeError() {
    employeeRepeatError.value = true;
    setTimeout(() => {
        employeeRepeatError.value = false;
    }, 3000);
}

function showFormError(errorMessage) {
    formErrorState.value = true;
    formErrorMessage.value = errorMessage;

    setTimeout(() => {
        formErrorState.value = false;
        formErrorMessage.value = "";
    }, 3000);
}

async function removeProject() {
    const response = await axios.post(
        "api/delete_project",
        {
            project_name: projectName.value,
        },
        { headers: { Authorization: `Bearer ${store.token}` } }
    );
    console.log(response);

    if (!(response.data.status < 400 || response.data.message === "Successful"))
        return false;
    return true;
}

async function updateInitProjectStatus(token) {
    const response = await axios.post(
        `api/update_project_status`,
        {
            project_name: projectName.value,
            new_status: "Unfinished",
        },
        { headers: { Authorization: `Bearer ${token}` } }
    );
    if (response.data.status < 400 || response.data.message === "Successful") {
        return true;
    }
    return false;
}

async function addEmployee(token, employeeUsername) {
    const response = await axios.post(
        `api/add_employee_to_project`,
        {
            project_name: projectName.value,
            employee_username: employeeUsername,
        },
        { headers: { Authorization: `Bearer ${token}` } }
    );
    console.log(response);
    if (response.data.status < 400 || response.data.message === "Successful") {
        return true;
    }
    return false;
}

async function addNewProject(token) {
    let isEmployeeAdded;

    console.log(projectName.value, description.value, token);
    const response = await axios.post(
        `api/add_new_project`,
        {
            project_name: projectName.value,
            description: description.value,
        },
        { headers: { Authorization: `Bearer ${token}` } }
    );
    console.log(response);

    if (
        !(response.data.status < 400 || response.data.message === "Successful")
    ) {
        showFormError(
            "Something went wrong. Possibly project with this name does exist!"
        );
        return;
    }

    const isStatusUpdated = await updateInitProjectStatus(token);
    if (!isStatusUpdated) {
        showFormError("Something went wrong.");
        await removeProject();
        return;
    }

    store.currentProject.name = projectName.value;
    store.currentProject.status = "Unfinished";

    for (const empData of employeeList.value) {
        isEmployeeAdded = await addEmployee(token, empData.username);
        console.log("this " + isEmployeeAdded);
        if (!isEmployeeAdded) {
            showFormError("Could not add employee " + empData.username);
            await removeProject();
            return;
        }
    }

    router.push({ name: "homeEmployer" });
}

async function validate() {
    const { valid } = await form.value.validate();
    if (!valid) return;
    if (!employeeList.value.length) {
        showFormError("Project should have at least one employee.");
        return;
    }
    addNewProject(store.token);
}

async function AddValidEmp() {
    const { valid } = await empForm.value.validate();
    if (!valid) return;
    const employeeExists = employeeList.value.filter(
        (emp) => emp.username === username.value
    );
    if (employeeExists.length) {
        showEmployeeError();
        return;
    }
    const employeeData = {
        username: username.value,
        payment: payment.value,
    };

    employeeList.value.push(employeeData);
    empForm.value.reset();
}

function removeEmployee(empData) {
    const empIndex = employeeList.value.findIndex(
        (emp) => emp.username === empData.username
    );
    employeeList.value.splice(empIndex, 1);
}

onMounted(() => {
    useInitData();
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
                    @click="router.push({ name: 'homeEmployer' })"
                ></v-btn>
            </template>

            <v-app-bar-title>Add project</v-app-bar-title>

            <template v-slot:append>
                <v-btn
                    icon="mdi-check"
                    size="large"
                    color="success"
                    class="text-h6"
                    @click="validate"
                ></v-btn>
            </template>
        </v-app-bar>
        <v-main>
            <v-container>
                <v-form
                    ref="form"
                    @submit.prevent
                    lazy-validation
                    class="px-4 pt-4 pt-6"
                >
                    <v-text-field
                        v-model="projectName"
                        variant="filled"
                        :rules="namingRules"
                        color="light-blue-darken-4"
                        label="Project Name"
                    ></v-text-field>
                    <v-textarea
                        auto-grow
                        v-model="description"
                        variant="filled"
                        :rules="namingRules"
                        color="light-blue-darken-4"
                        label="Description"
                    ></v-textarea>
                </v-form>

                <v-alert
                    v-if="formErrorState"
                    density="comfortable"
                    type="error"
                    class="mb-5"
                >
                    {{ formErrorMessage }}
                </v-alert>

                <v-divider></v-divider>

                <v-form
                    ref="empForm"
                    @submit.prevent
                    lazy-validation
                    class="px-4 py-4"
                >
                    <v-row>
                        <v-col cols="6">
                            <v-text-field
                                v-model="username"
                                :rules="namingRules"
                                variant="filled"
                                color="light-blue-darken-4"
                                label="Employee username"
                            >
                            </v-text-field>
                        </v-col>
                        <v-col cols="4">
                            <v-text-field
                                v-model="payment"
                                :rules="[positiveRule]"
                                variant="filled"
                                color="light-blue-darken-4"
                                label="Payment / Hour"
                                type="number"
                                min="0"
                                append-inner-icon="mdi-currency-usd"
                            >
                            </v-text-field>
                        </v-col>
                        <v-col>
                            <v-btn
                                icon="mdi-plus"
                                color="light-blue"
                                @click="AddValidEmp"
                            ></v-btn>
                        </v-col>
                    </v-row>
                </v-form>

                <v-alert
                    v-if="employeeRepeatError"
                    density="comfortable"
                    type="error"
                    class="mb-5"
                >
                    Employee with this username does exist.
                </v-alert>

                <v-list lines="one">
                    <v-list-subheader>Employees</v-list-subheader>

                    <v-list-item
                        v-for="emp in employeeList"
                        :key="emp.username"
                        :title="emp.username"
                        :subtitle="`Payment per hour: ${emp.payment}$`"
                        class="mb-3"
                    >
                        <template v-slot:append>
                            <v-btn
                                color="grey-darken-1"
                                icon="mdi-close"
                                @click="removeEmployee(emp)"
                                size="small"
                                variant="tonal"
                            ></v-btn>
                        </template>
                    </v-list-item>
                </v-list>
            </v-container>
        </v-main>
    </v-app>
</template>
