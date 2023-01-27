<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";
import { useInitData } from "../composables/initData";

onMounted(() => {
    const router = useRouter();
    const role = useInitData();
    if (role === "employee") router.push({ name: "homeEmployee" });
    else if (role === "employer") router.push({ name: "homeEmployer" });
    else router.push("/login");
});
</script>

<template>
    <div>
        <h3>Hello</h3>
    </div>
</template>

<!-- <script>
// import axios from "axios";

export default {
    // async created() {
    //     const response = await axios.get("test", {
    //         headers: {
    //             Authorization: "Bearer" + this.$cookies.get("csrftoken"),
    //         },
    //     });
    //     console.log(response);
    // },
};
</script> -->

<style scoped>
div {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #eee;
    padding: 1rem;
    border-radius: 12px;
    width: 40%;
    margin: auto;
}
</style>
