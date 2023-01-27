import axios from "axios";
import { useRouter } from "vue-router";
import { ref } from "vue";
import { useUserStore } from "../stores/user";

export function useLogin(userRoleRef) {
    const router = useRouter();

    const username = ref("");
    const password = ref("");
    const errorMessage = ref("");
    const showError = ref(false);

    function updateInfo(info) {
        console.log(info);
        const [usernameVal, passwordVal] = info;
        username.value = usernameVal;
        password.value = passwordVal;
    }

    async function getSubmitData() {
        console.log(username, password);
        const response = await axios.post(`api/login_${userRoleRef.value}`, {
            username: username.value,
            password: password.value,
        });

        console.log(response);
        if (
            response.data.message === "Successful" ||
            response.data.access_token
        ) {
            const accessToken = response.data.access_token;
            localStorage.setItem("access_token", accessToken);
            localStorage.setItem("user_role", userRoleRef.value);
            const store = useUserStore();
            store.role = userRoleRef.value;
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

    return {
        username,
        password,
        errorMessage,
        showError,
        updateInfo,
        getSubmitData,
    };
}
