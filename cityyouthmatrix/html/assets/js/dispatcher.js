"use strict";
/// <reference path="../typings/global.d.ts" />
exports.__esModule = true;
exports.dispatch = void 0;
var core_1 = require("@fullcalendar/core");
var google_calendar_1 = require("@fullcalendar/google-calendar");
function dispatch() {
    if (document.querySelectorAll(".datatable").length > 0 &&
        document.querySelectorAll(".datatable2").length > 0) {
        var dataTable = new DataTable(".datatable", {
            perPage: 10
        });
        var dataTable = new DataTable(".datatable2", {
            perPage: 10
        });
    }
    // var dataTable = new DataTable(".datatable3",{
    // 	perPage:10
    // });
    // var dataTable = new DataTable(".datatable4",{
    // 	perPage:10
    // });
    // init calendar
    var calendarEl = document.getElementById("calendar");
    if (calendarEl != undefined) {
        var calendar = new core_1.Calendar(calendarEl, {
            plugins: [google_calendar_1["default"]],
            googleCalendarApiKey: "AIzaSyDzWcZv7q04t-8hbr2TkbKr-XFdKBJbMAs",
            events: {
                googleCalendarId: "od9mode2m7q35qqi7u968pdfuk@group.calendar.google.com"
            }
        });
        calendar.render();
    }
}
exports.dispatch = dispatch;
