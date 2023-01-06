<script setup></script>

<template>
    <v-app class="bg-light-blue-lighten-5">
        <v-main>
            <div class="timestamp text-center mt-8">
                <h2 class="text-h4">00:00</h2>
                <h3 class="text-h5">Friday, 6 January</h3>
            </div>

            <v-sheet
                class="d-flex flex-no-wrap justify-space-between align-center px-5 mx-auto mt-12"
                style="background-color: #e1e2fe"
                height="100"
                width="80%"
                rounded
                elevation="3"
            >
                <p class="text-h6">Add a new project</p>

                <v-btn
                    icon="mdi-plus"
                    size="x-large"
                    class="bg-grey-lighten-5"
                ></v-btn>
            </v-sheet>

            <v-sheet
                class="mx-auto mt-10"
                width="80%"
                style="background-color: #e1e2fe"
                rounded
                elevation="3"
            >
                <v-container>
                    <v-row align="center">
                        <v-col cols="8"
                            ><div class="text-h5 text-light-blue-darken-4">
                                <span>Title</span>
                            </div></v-col
                        >
                        <v-col cols="4"
                            ><div><span>Status:</span><span>--</span></div>
                        </v-col>
                    </v-row>
                </v-container>
            </v-sheet>
            <section class="w-75 mx-auto mt-7">
                <div class="text-subtitle-1 d-flex justify-space-between">
                    <span>Employees</span>
                    <v-icon>mdi-pencil</v-icon>
                </div>
                <v-divider></v-divider>
                <div class="employees"></div>
            </section>
        </v-main>
    </v-app>
</template>
