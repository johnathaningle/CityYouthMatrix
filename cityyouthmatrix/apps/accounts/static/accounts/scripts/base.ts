import { M } from "../typings/init";


document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');

    var instances = M.Sidenav.init(elems, {
        edge:'left'
    });

    var elems = document.querySelectorAll('.tabs');
    var instance = M.Tabs.init(elems,  {
    	swipeable:false
    });
});