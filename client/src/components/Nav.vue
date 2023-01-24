<template>
    <nav>
        <router-link to="/" class="home">Home</router-link>
        <ul class="nav-menu">
            <li class="nav-item">
                <router-link to="/employee/login" class="nav-link"
                    >Enter as employee</router-link
                >
            </li>
            <li class="nav-item">
                <router-link to="/employer/login" class="nav-link"
                    >Enter as employer</router-link
                >
            </li>
        </ul>
    </nav>
</template>

<script>
export default {
    name: "nav-bar",
};
</script>

<style scoped>
nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #333;
    background-color: #eee;
    padding: 2rem 4rem;
}

.nav-menu {
    display: flex;
    align-items: center;
    gap: 4rem;
}

.nav-item {
    list-style: none;
    font-size: 1.2rem;
}

.nav-link:link,
.nav-link:visited {
    text-decoration: none;
    color: inherit;
}

.home:link,
.home:visited {
    text-decoration: none;
    color: inherit;
    font-size: 1.8rem;
}
</style>
