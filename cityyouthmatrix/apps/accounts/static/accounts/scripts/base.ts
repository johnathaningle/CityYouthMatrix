import { M } from "../typings/init";


document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');

    var instances = M.Sidenav.init(elems, {
        edge:'left'
    });

});