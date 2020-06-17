import { DataTable, FullCalendar } from "../typings/init";

document.addEventListener("DOMContentLoaded", function() {
    var dataTable = new DataTable(".datatable",{
        perPage:10
    });
    var dataTable = new DataTable(".datatable2",{
        perPage:10
    });
    // var dataTable = new DataTable(".datatable3",{
    // 	perPage:10
    // });
    // var dataTable = new DataTable(".datatable4",{
    // 	perPage:10
    // });
    // init calendar
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: [ 'dayGrid' ]
    });

    calendar.render();
});

