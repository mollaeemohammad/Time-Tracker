import Vue from "vue";
import cors from "cors";

const corsOptions = {
    origin: "http://localhost:3000",
    credentials: true, //access-control-allow-credentials:true
    optionSuccessStatus: 200,
};

Vue.use(cors());
