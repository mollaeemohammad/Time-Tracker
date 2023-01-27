import { useUserStore } from "../stores/user";
import jwt_decode from "jwt-decode";

export function useInitData() {
    const accessToken = localStorage.getItem("access_token");
    const userRole = localStorage.getItem("user_role");
    const store = useUserStore();
    if (accessToken && userRole) {
        console.log(accessToken);
        const decoded = jwt_decode("Bearer " + accessToken);
        store.username = decoded.sub;
        store.role = userRole;
        store.token = accessToken;

        const projectInfo = localStorage.getItem(`${userRole}_project`);
        if (projectInfo) store.currentProject = JSON.parse(projectInfo);
        else store.currentProject = "";

        console.log(decoded);
        console.log(store.username, store.role);
        return userRole;
    }
    return null;
}
