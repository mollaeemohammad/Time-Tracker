<script setup>
import axios from "axios";
import { useRouter } from "vue-router";
import { ref } from "vue";

const router = useRouter();

const firstName = ref("");
const lastName = ref("");
const username = ref("");
const password = ref("");
const passwordConfirm = ref("");
const showError = ref(false);
const errorMessage = ref("");

async function getSubmitData() {
    const response = await axios.post("api/signup_employer", {
        first_name: firstName.value,
        last_name: lastName.value,
        username: username.value,
        password: password.value,
        confirm_password: passwordConfirm.value,
    });
    console.log(response);

    if (response.data.message === "Successful") {
        router.push("/employer/login");
    }

    if (response.data.status >= 400) {
        showError.value = true;
        errorMessage.value = response.data.message;
        setTimeout(() => {
            showError.value = false;
        }, 3000);
    }
}
</script>

<template>
    <div class="container">
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
