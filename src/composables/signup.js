import axios from "axios";
import { useRouter } from "vue-router";
import { ref } from "vue";

export function useSignup(userRole) {
    const router = useRouter();

    const firstName = ref("");
    const lastName = ref("");
    const username = ref("");
    const password = ref("");
    const passwordConfirm = ref("");
    const showError = ref(false);
    const errorMessage = ref("");

    function updateInfo(info) {
        const [
            firstNameVal,
            lastNameVal,
            usernameVal,
            passwordVal,
            passwordConfirmVal,
        ] = info;

        firstName.value = firstNameVal;
        lastName.value = lastNameVal;
        username.value = usernameVal;
        password.value = passwordVal;
        passwordConfirm.value = passwordConfirmVal;
    }

    async function getSubmitData() {
        const response = await axios.post(`api/signup_${userRole}`, {
            first_name: firstName.value,
            last_name: lastName.value,
            username: username.value,
            password: password.value,
            confirm_password: passwordConfirm.value,
        });
        console.log(response);

        if (response.data.message === "Successful") {
            router.push(`/${userRole}/login`);
        }

        if (response.data.status >= 400) {
            showError.value = true;
            errorMessage.value = response.data.message;
            setTimeout(() => {
                showError.value = false;
            }, 3000);
        }
    }

    return {
        firstName,
        lastName,
        username,
        password,
        passwordConfirm,
        showError,
        errorMessage,
        updateInfo,
        getSubmitData,
    };
}
