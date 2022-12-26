<script setup>
import axios from "axios";
import { useRouter } from "vue-router";
import { ref } from "vue";

const router = useRouter();

const username = ref("");
const password = ref("");
const errorMessage = ref("");
const showError = ref(false);

async function getSubmitData() {
    const response = await axios.post("api/login_employee", {
        username: username.value,
        password: password.value,
    });

    console.log(response);
    if (response.data.message === "Successful") {
        router.push("/");
    } else if (
        response.data.message === "Unsuccessful" ||
        response.data?.status === 401
    ) {
        errorMessage.value = "Username or password is wrong";
        showError.value = true;

        setTimeout(() => {
            showError.value = false;
        }, 3000);
    }
}
</script>

<template>
    <div class="container">
        <h3>Employee Login</h3>
        <form @submit.prevent="getSubmitData">
            <div class="inputs">
                <p class="error" v-show="showError">{{ errorMessage }}</p>
                <div class="input-container">
                    <input
                        type="text"
                        name="employee-uname"
                        id="employee-uname"
                        placeholder="Username"
                        v-model="username"
                        required
                    />
                </div>
                <div class="input-container">
                    <input
                        type="password"
                        name="password"
                        id="password"
                        placeholder="Password"
                        v-model="password"
                        required
                    />
                </div>
            </div>
            <button>Login</button>
        </form>
        <p class="form-text">
            New employee? go to
            <router-link to="/employee/signup" class="form-link"
                >signup page</router-link
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
    font-size: 1.1rem;
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
