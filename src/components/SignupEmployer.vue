<script setup>
import SignupForm from "./signupForm.vue";
import { useSignup } from "../composables/signup";

const {
    firstName,
    lastName,
    username,
    password,
    passwordConfirm,
    showError,
    errorMessage,
    updateInfo,
    getSubmitData,
} = useSignup("employer");
</script>

<template>
    <SignupForm
        user-role="employer"
        :error-message="errorMessage"
        :show-error="showError"
        :update-info="updateInfo"
        :get-submit-data="getSubmitData"
    />
    <!-- <div class="container">
        <h3>Signup</h3>
        <form @submit.prevent="getSubmitData">
            <p class="error" v-show="showError">{{ errorMessage }}</p>

            <div class="inputs">
                <div class="input-container">
                    <input
                        type="text"
                        name="employer-fname"
                        id="employer-fname"
                        placeholder="First Name"
                        v-model="firstName"
                        required
                    />
                </div>
                <div class="input-container">
                    <input
                        type="text"
                        name="employer-lname"
                        id="employer-lname"
                        placeholder="Last Name"
                        v-model="lastName"
                        required
                    />
                </div>
                <div class="input-container">
                    <input
                        type="text"
                        name="employer-uname"
                        id="employer-uname"
                        placeholder="Employer Username"
                        v-model="username"
                        required
                    />
                </div>
                <div class="input-container">
                    <input
                        type="password"
                        name="employer-password"
                        id="employer-password"
                        placeholder="Password"
                        v-model="password"
                        required
                    />
                </div>
                <div class="input-container">
                    <input
                        type="password"
                        name="employer-password-confirm"
                        id="employer-password-confirm"
                        placeholder="Confirm Password"
                        v-model="passwordConfirm"
                        required
                    />
                </div>
            </div>
            <button>Signup</button>
        </form>
        <p class="form-text">
            Are you a registered employer? go to
            <router-link to="/employer/login" class="form-link"
                >login page</router-link
            >
        </p>
    </div> -->
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
