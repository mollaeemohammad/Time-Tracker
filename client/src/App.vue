<template>
    <div id="app">
        <Nav></Nav>
        <main>
            <section class="container">
                <!-- <AlertVue class="alert"></AlertVue> -->
                <router-view></router-view>
            </section>
        </main>
    </div>
</template>

<script>
import Nav from "./components/Nav.vue";

export default {
    name: "App",
    components: {
        Nav,
    },
};
</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: inherit;
}

body {
    box-sizing: border-box;
    height: 100vh;
    background-color: rgb(18, 162, 210);
    color: #333;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

.container {
    padding: 4rem 8rem;
}
</style>
