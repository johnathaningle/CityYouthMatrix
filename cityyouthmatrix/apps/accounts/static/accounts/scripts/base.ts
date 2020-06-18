
/// <reference path="../typings/global.d.ts" />

export function initDashboard() {
    var elems = document.querySelectorAll('.sidenav');

    var instances = M.Sidenav.init(elems, {
        edge:'left'
    });

    var elems = document.querySelectorAll('.tabs');
    if(elems.length > 0) {
        var instance = M.Tabs.init(elems,  {
            swipeable:false
        });
    }
}