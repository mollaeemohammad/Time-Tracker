<script setup>
import { ref, computed } from "vue";
import { RouterLink } from "vue-router";
import { useLogin } from "../composables/login";

const step = ref(1);
const roleRadios = ref(null);

const form = ref(null);
const {
    username,
    password,
    showError,
    errorMessage,
    updateInfo,
    getSubmitData,
} = useLogin(roleRadios);

const requiredRule = ref((v) => !!v || "This field is required");
const blankRule = ref((v) => (v && !!v.trim()) || "Value cannot be blank");
const namingRules = ref([requiredRule.value, blankRule.value]);

const currentTitle = computed(() => {
    return `I want to login as ${
        roleRadios.value ? `an ${roleRadios.value}` : "..."
    }`;
});

async function validate() {
    const { valid } = await form.value.validate();

    if (!valid) return;

    updateInfo([username.value, password.value]);
    getSubmitData();
}
</script>

<template>
    <v-container fluid class="fill-height">
        <v-row justify="center" align="center" style="height: 100vh">
            <v-col>
                <v-card class="mx-auto" max-width="500">
                    <v-card-title
                        class="text-h6 font-weight-regular justify-space-between"
                    >
                        <span>{{ currentTitle }}</span>
                    </v-card-title>

                    <v-window v-model="step">
                        <v-window-item :value="1">
                            <v-radio-group v-model="roleRadios" mandatory>
                                <v-radio
                                    label="Employee"
                                    value="employee"
                                ></v-radio>
                                <v-radio
                                    label="Employer"
                                    value="employer"
                                ></v-radio>
                            </v-radio-group>
                        </v-window-item>

                        <v-window-item :value="2">
                            <v-card-text>
                                <v-alert
                                    v-if="showError"
                                    density="comfortable"
                                    type="error"
                                    class="mb-5"
                                >
                                    {{ errorMessage }}
                                </v-alert>

                                <v-form
                                    ref="form"
                                    @submit.prevent
                                    lazy-validation
                                >
                                    <v-text-field
                                        v-model="username"
                                        label="Username"
                                        :rules="namingRules"
                                        color="light-blue-darken-4"
                                    ></v-text-field>

                                    <v-text-field
                                        v-model="password"
                                        label="Password"
                                        type="password"
                                        :rules="[
                                            requiredRule,
                                            (p) =>
                                                p.length >= 8 ||
                                                'Password should have at least 8 characters',
                                        ]"
                                        color="light-blue-darken-4"
                                    ></v-text-field>
                                </v-form>
                            </v-card-text>
                        </v-window-item>
                    </v-window>

                    <v-divider></v-divider>

                    <v-card-actions>
                        <v-btn v-if="step > 1" variant="text" @click="step--">
                            Back
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                            v-if="step < 3"
                            color="primary"
                            variant="flat"
                            @click="
                                if (step === 1) {
                                    // initData();
                                    step++;
                                } else if (step === 2) validate();
                            "
                            :disabled="!roleRadios"
                        >
                            {{ step === 1 ? "Next" : "Login" }}
                        </v-btn>
                    </v-card-actions>
                </v-card>
                <p class="text-subtitle-1 mt-5 text-center">
                    New here? go to
                    <router-link to="signup" class="text-decoration-none"
                        >signup</router-link
                    >
                    page
                </p>
            </v-col>
        </v-row>
    </v-container>
</template>
