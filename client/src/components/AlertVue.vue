<template>
    <div>
        <h3>Hello</h3>
    </div>
</template>

<script>
// import axios from "axios";

export default {
    name: "alert-vue",

    // async created() {
    //     const response = await axios.get("test", {
    //         headers: {
    //             Authorization: "Bearer" + this.$cookies.get("csrftoken"),
    //         },
    //     });
    //     console.log(response);
    // },
};
</script>

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
