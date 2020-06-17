import { dispatch } from "./dispatcher";
import { initDashboard } from "./base";

document.addEventListener("DOMContentLoaded", function() {
    initDashboard();
    dispatch();
});