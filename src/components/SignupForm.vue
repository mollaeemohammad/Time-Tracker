<script setup>
import { ref } from "vue";

const props = defineProps([
    "userRole",
    "errorMessage",
    "showError",
    "updateInfo",
    "getSubmitData",
]);
const localFirstName = ref("");
const localLastName = ref("");
const localUsername = ref("");
const localPassword = ref("");
const localPasswordConfirm = ref("");

const userRoleCapital =
    props.userRole.charAt(0).toUpperCase() + props.userRole.slice(1);
</script>

<template>
    <div class="container">
        <h3>{{ userRoleCapital }} Signup</h3>
        <form
            @submit.prevent="
                updateInfo([
                    localFirstName,
                    localLastName,
                    localUsername,
                    localPassword,
                    localPasswordConfirm,
                ]);
                getSubmitData();
            "
        >
            <div class="inputs">
                <p class="error" v-show="showError">{{ errorMessage }}</p>
                <div class="input-container">
                    <input
                        type="text"
                        :name="`${userRole}-fname`"
                        :id="`${userRole}-fname`"
                        placeholder="First Name"
                        v-model="localFirstName"
                        required
                    />
                </div>
                <div class="input-container">
                    <input
                        type="text"
                        :name="`${userRole}-lname`"
                        :id="`${userRole}-lname`"
                        placeholder="Last Name"
                        v-model="localLastName"
                        required
                    />
                </div>
                <div class="input-container">
                    <input
                        type="text"
                        :name="`${userRole}-uname`"
                        :id="`${userRole}-uname`"
                        placeholder="Username"
                        v-model="localUsername"
                        required
                    />
                </div>
                <div class="input-container">
                    <input
                        type="password"
                        :name="`${userRole}-password`"
                        :id="`${userRole}-password`"
                        placeholder="Password"
                        v-model="localPassword"
                        required
                    />
                </div>
                <div class="input-container">
                    <input
                        type="password"
                        :name="`${userRole}-password-confirm`"
                        :id="`${userRole}-password-confirm`"
                        placeholder="Confirm Password"
                        v-model="localPasswordConfirm"
                        required
                    />
                </div>
            </div>
            <button>Signup</button>
        </form>
        <p class="form-text">
            Already an {{ userRole }}? go to
            <router-link :to="`/${userRole}/login`" class="form-link"
                >login page</router-link
            >
        </p>
    </div>
</template>

<style scoped>
.container {
    background-color: #eee;
    color: #333;
    padding: 2rem 4rem;
    border-radius: 12px;
    text-align: center;
    width: 40%;
    margin: auto;
}

.error {
    background-color: rgba(230, 63, 63, 0.7);
    color: #eee;
    border-radius: 12px;
    padding: 0.5rem;
    margin-bottom: 1rem;
}

.inputs {
    margin: 2.5rem auto 1.5rem;
}

.input-container {
    text-align: center;
}

input {
    border-radius: 100rem;
    border: 1px solid #aaa;
    padding: 1rem 2rem;
    margin: 0.5rem 0;
    width: 100%;
    font-size: 1rem;
}

button {
    border: none;
    border-radius: 100rem;
    color: #eee;
    width: 100%;
    padding: 1rem 2rem;
    background-color: rgb(20, 144, 185);
    font-size: 1.2rem;
    font-weight: 700;
}

button:hover {
    cursor: pointer;
    background-color: rgb(24, 119, 151);
}

.form-text {
    margin-top: 0.5rem;
}

.form-link:link,
.form-link:visited {
    color: rgb(20, 144, 185);
    text-decoration: none;
}
</style>
