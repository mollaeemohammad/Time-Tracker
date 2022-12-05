<template>
    <div class="container">
        <h3>Signup</h3>
        <form @submit.prevent="getSubmitData">
            <div class="inputs">
                <p class="error" v-show="showError">{{ errorMessage }}</p>
                <div class="input-container">
                    <input
                        type="text"
                        name="employee-fname"
                        id="employee-fname"
                        placeholder="First Name"
                        v-model="firstName"
                        required
                    />
                </div>
                <div class="input-container">
                    <input
                        type="text"
                        name="employee-lname"
                        id="employee-lname"
                        placeholder="Last Name"
                        v-model="lastName"
                        required
                    />
                </div>
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
                        name="employee-password"
                        id="employee-password"
                        placeholder="Password"
                        v-model="password"
                        required
                    />
                </div>
                <div class="input-container">
                    <input
                        type="password"
                        name="employee-password-confirm"
                        id="employee-password-confirm"
                        placeholder="Confirm Password"
                        v-model="passwordConfirm"
                        required
                    />
                </div>
            </div>
            <button>Signup</button>
        </form>
        <p class="form-text">
            Already an employee? go to
            <router-link to="/employee/login" class="form-link"
                >login page</router-link
            >
        </p>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "signup-empolyee",
    data() {
        return {
            firstName: "",
            lastName: "",
            username: "",
            password: "",
            passwordConfirm: "",
            showError: false,
            errorMessage: "",
        };
    },
    methods: {
        async getSubmitData() {
            const response = await axios.post("api/signup_employee", {
                first_name: this.firstName,
                last_name: this.lastName,
                username: this.username,
                password: this.password,
                confirm_password: this.passwordConfirm,
            });
            console.log(response);

            if (response.data.message === "Successful") {
                this.$router.push("/employee/login");
            }

            if (response.data.status >= 400) {
                this.showError = true;
                this.errorMessage = response.data.message;
                setTimeout(() => {
                    this.showError = false;
                }, 3000);
            }
        },
    },
};
</script>

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
