<script setup>
import axios from "axios";
import { ref, computed, onMounted } from "vue";
import { useInitData } from "../composables/initData";
import router from "../router";
import { useUserStore } from "../stores/user";

const role = useInitData();
const store = useUserStore();
const fullName = ref("");
const major = ref("");
const phone = ref("");
const email = ref("");
const readOnly = ref(false);
const editable = ref(false);
const deleteDialog = ref(false);

major.value = "Designer";
readOnly.value = true;

const activeEdit = function () {
    editable.value = true;
    readOnly.value = false;
};

const deactiveEdit = function () {
    editable.value = false;
    readOnly.value = true;
};

async function getUser() {
    const response = await axios.post(
        `api/get_${role}`,
        {
            username: store.username,
        },
        { headers: { Authorization: `Bearer ${store.token}` } }
    );
    console.log(response);

    if (response.data && !response.data.status) {
        fullName.value = response.data[2] + " " + response.data[1];
        console.log(fullName.value);
    }
}

async function logout() {}

async function deleteUser() {
    const response = await axios.post(
        `api/delete_${role}`,
        {},
        { headers: { Authorization: `Bearer ${store.token}` } }
    );
    console.log(response);
    router.push({ name: "login" });
}

onMounted(() => {
    getUser();
});
</script>

<template>
    <v-app style="height: 90vh">
        <v-main>
            <v-container>
                <v-card max-width="800" class="mx-auto my-8">
                    <v-card-text class="text-center">
                        <v-row
                            justify="space-around"
                            align="center"
                            class="mb-5"
                        >
                            <v-col cols="6">
                                <v-avatar color="info" size="100">
                                    <v-icon>mdi-pencil</v-icon>
                                </v-avatar>
                            </v-col>
                            <v-col cols="6" class="text-left">
                                <div class="text-h5">
                                    {{ fullName || "Full Name" }}
                                </div>
                                <div class="text-caption">
                                    @{{ store.username }}
                                </div>
                            </v-col>
                        </v-row>
                        <v-row justify="space-around" align="center">
                            <v-col cols="12">
                                <v-text-field
                                    label="Major"
                                    variant="outlined"
                                    v-model="major"
                                    :readonly="readOnly"
                                ></v-text-field>
                                <v-text-field
                                    label="Phone"
                                    variant="outlined"
                                    v-model="phone"
                                    :readonly="readOnly"
                                ></v-text-field>
                                <v-text-field
                                    label="Email"
                                    type="email"
                                    variant="outlined"
                                    v-model="email"
                                    :readonly="readOnly"
                                ></v-text-field>
                            </v-col>
                        </v-row>
                    </v-card-text>
                    <v-card-actions>
                        <v-row justify="center" v-if="!editable">
                            <v-col cols="12" class="text-center">
                                <v-btn
                                    rounded="4"
                                    variant="tonal"
                                    color="primary"
                                    width="50%"
                                    height="50"
                                    class="mx-auto"
                                    @click="activeEdit"
                                >
                                    Edit Profile
                                </v-btn>
                            </v-col>

                            <v-col cols="12" class="text-center">
                                <v-btn
                                    rounded="4"
                                    variant="outlined"
                                    color="info"
                                    width="50%"
                                    height="50"
                                    class="mx-auto"
                                >
                                    Logout
                                </v-btn>
                            </v-col>

                            <v-col cols="12" class="text-center">
                                <v-btn
                                    rounded="4"
                                    variant="outlined"
                                    color="error"
                                    width="50%"
                                    height="50"
                                >
                                    Delete Account

                                    <v-dialog
                                        v-model="deleteDialog"
                                        max-width="800"
                                        activator="parent"
                                    >
                                        <v-card>
                                            <v-card-text>
                                                Are you sure you want to delete
                                                this account?
                                            </v-card-text>
                                            <v-card-actions>
                                                <v-row>
                                                    <v-col
                                                        cols="6"
                                                        class="text-center pa-0"
                                                    >
                                                        <v-btn
                                                            color="error"
                                                            block
                                                            variant="tonal"
                                                            @click="
                                                                deleteDialog = false;
                                                                deleteUser();
                                                            "
                                                            >Delete</v-btn
                                                        >
                                                    </v-col>
                                                    <v-col
                                                        cols="6"
                                                        class="text-center pa-0"
                                                    >
                                                        <v-btn
                                                            color="info"
                                                            block
                                                            variant="tonal"
                                                            @click="
                                                                deleteDialog = false
                                                            "
                                                            >Cancel</v-btn
                                                        >
                                                    </v-col>
                                                </v-row>
                                            </v-card-actions>
                                        </v-card>
                                    </v-dialog>
                                </v-btn>
                            </v-col>
                        </v-row>
                        <v-row no-gutters v-else>
                            <v-col cols="9">
                                <v-btn
                                    rounded="0"
                                    color="primary"
                                    variant="tonal"
                                    width="100%"
                                    height="50"
                                    @click="deactiveEdit"
                                >
                                    Save
                                </v-btn>
                            </v-col>
                            <v-col cols="3">
                                <v-btn
                                    rounded="0"
                                    color="primary"
                                    width="100%"
                                    height="50"
                                    @click="deactiveEdit"
                                >
                                    Cancel
                                </v-btn>
                            </v-col>
                        </v-row>
                    </v-card-actions>
                </v-card>
            </v-container>
        </v-main>
    </v-app>
</template>
