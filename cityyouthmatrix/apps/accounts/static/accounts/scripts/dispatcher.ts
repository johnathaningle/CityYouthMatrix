
/// <reference path="../typings/global.d.ts" />

export function dispatch() {

    if(document.querySelectorAll(".datatable").length > 0 && document.querySelectorAll(".datatable2").length > 0) {
        var dataTable = new DataTable(".datatable",{
            perPage:10
        });
        var dataTable = new DataTable(".datatable2",{
            perPage:10
        });
    }

    // var dataTable = new DataTable(".datatable3",{
    // 	perPage:10
    // });
    // var dataTable = new DataTable(".datatable4",{
    // 	perPage:10
    // });
    // init calendar
    var calendarEl = document.getElementById('calendar');

    if(calendarEl != undefined) {
        var calendar = new FullCalendar.Calendar(calendarEl, {
            plugins: [ 'dayGrid', 'googleCalendar' ],
            googleCalendarApiKey: '<YOUR API KEY>',
            events: {
                googleCalendarId: 'abcd1234@group.calendar.google.com',
                className: 'gcal-event' // an option!
            }
        });
    
        calendar.render();
    }
}

