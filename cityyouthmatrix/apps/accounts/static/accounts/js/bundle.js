!function(e){var t={};function n(r){if(t[r])return t[r].exports;var o=t[r]={i:r,l:!1,exports:{}};return e[r].call(o.exports,o,o.exports,n),o.l=!0,o.exports}n.m=e,n.c=t,n.d=function(e,t,r){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(n.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)n.d(r,o,function(t){return e[t]}.bind(null,o));return r},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s=0)}([function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=n(1),o=n(2);document.addEventListener("DOMContentLoaded",(function(){o.initDashboard(),r.dispatch()}))},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.dispatch=void 0,t.dispatch=function(){if(document.querySelectorAll(".datatable").length>0&&document.querySelectorAll(".datatable2").length>0)new DataTable(".datatable",{perPage:10}),new DataTable(".datatable2",{perPage:10});var e=document.getElementById("calendar");null!=e&&new FullCalendar.Calendar(e,{plugins:["dayGrid","googleCalendar"],googleCalendarApiKey:"AIzaSyDzWcZv7q04t-8hbr2TkbKr-XFdKBJbMAs",events:{googleCalendarId:"od9mode2m7q35qqi7u968pdfuk@group.calendar.google.com"}}).render()}},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.initDashboard=void 0,t.initDashboard=function(){var e=document.querySelectorAll(".sidenav");if(M.Sidenav.init(e,{edge:"left"}),e=document.querySelectorAll(".modal"),M.Modal.init(e,{opacity:.5}),(e=document.querySelectorAll(".tabs")).length>0)M.Tabs.init(e,{swipeable:!1});e=document.querySelectorAll(".select"),M.FormSelect.init(e,{}),e=document.querySelectorAll(".timepicker"),M.Timepicker.init(e,{}),e=document.querySelectorAll(".datepicker"),M.Datepicker.init(e,{}),e=document.querySelectorAll(".dropdown-trigger"),M.Dropdown.init(e,{})}}]);