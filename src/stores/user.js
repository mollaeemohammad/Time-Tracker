import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { useRouter } from "vue-router";

export const useUserStore = defineStore("user", () => {
    const router = useRouter();
    const token = ref("");
    const username = ref("");
    const role = ref("");
    const projects = ref([]);
    const currentProject = ref({});
    const currentRouteName = computed(() => router.currentRoute.value.name);

    return {
        token,
        username,
        role,
        projects,
        currentProject,
        currentRouteName,
    };
});
