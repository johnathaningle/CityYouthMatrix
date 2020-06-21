import { initDashboard } from "./base";
import  DispatcherController  from "./controllers/dispatcher/dispatcher";
import DriverController from "./controllers/driver/driver";

document.addEventListener("DOMContentLoaded", function() {
    initDashboard();
    var app = new Application();
});

class Application {
    constructor() {
        let page = location.pathname;
        let app: IController = null;
        switch(page) {
            case "/driver/driver":
                app = new DriverController();
        }
        if (app == null) {
            app = new DispatcherController();
        }
        app.handleLogic();
    }
}