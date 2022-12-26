<script setup>
import Nav from "./components/Nav.vue";
</script>

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

<style>
/* body {
    box-sizing: border-box;
    background-color: rgb(18, 162, 210);
    color: #333;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
} */

.container {
    padding: 4rem 8rem;
}
</style>
