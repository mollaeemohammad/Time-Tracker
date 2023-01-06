<script setup>
import { ref } from "vue";

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

async function validate() {
    const { valid } = await form.value.validate();
    if (!valid) return;
    if (!employeeList.value.length) {
        showFormError("Project should have at least one employee.");
        return;
    }
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

    employeeList.value.pop(empIndex);
}
</script>

<template>
    <v-app class="bg-light-blue-lighten-5">
        <v-app-bar>
            <template v-slot:prepend>
                <v-btn
                    icon="mdi-chevron-left"
                    size="large"
                    class="text-h6"
                    to="home"
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
