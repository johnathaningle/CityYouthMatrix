/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./scripts/app.ts");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./scripts/app.ts":
/*!************************!*\
  !*** ./scripts/app.ts ***!
  \************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\r\nObject.defineProperty(exports, \"__esModule\", { value: true });\r\nvar base_1 = __webpack_require__(/*! ./base */ \"./scripts/base.ts\");\r\nvar dispatcher_1 = __webpack_require__(/*! ./controllers/dispatcher/dispatcher */ \"./scripts/controllers/dispatcher/dispatcher.ts\");\r\nvar driver_1 = __webpack_require__(/*! ./controllers/driver/driver */ \"./scripts/controllers/driver/driver.ts\");\r\ndocument.addEventListener(\"DOMContentLoaded\", function () {\r\n    base_1.initDashboard();\r\n    var app = new Application();\r\n});\r\nvar Application = /** @class */ (function () {\r\n    function Application() {\r\n        var page = location.pathname;\r\n        var app = null;\r\n        switch (page) {\r\n            case \"/driver/driver\":\r\n                app = new driver_1.default();\r\n        }\r\n        if (app == null) {\r\n            app = new dispatcher_1.default();\r\n        }\r\n        app.handleLogic();\r\n    }\r\n    return Application;\r\n}());\r\n\n\n//# sourceURL=webpack:///./scripts/app.ts?");

/***/ }),

/***/ "./scripts/base.ts":
/*!*************************!*\
  !*** ./scripts/base.ts ***!
  \*************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\r\n/// <reference path=\"../typings/global.d.ts\" />\r\nObject.defineProperty(exports, \"__esModule\", { value: true });\r\nexports.initDashboard = void 0;\r\nfunction initDashboard() {\r\n    var elems = document.querySelectorAll('.sidenav');\r\n    var instances = M.Sidenav.init(elems, {\r\n        edge: 'left'\r\n    });\r\n    var elems = document.querySelectorAll('.modal');\r\n    var instance = M.Modal.init(elems, {\r\n        opacity: .5\r\n    });\r\n    var elems = document.querySelectorAll('.tabs');\r\n    if (elems.length > 0) {\r\n        var instance = M.Tabs.init(elems, {\r\n            swipeable: false\r\n        });\r\n    }\r\n    var elems = document.querySelectorAll('.select');\r\n    var instance = M.FormSelect.init(elems, {});\r\n    var elems = document.querySelectorAll('.timepicker');\r\n    var instance = M.Timepicker.init(elems, {});\r\n    var elems = document.querySelectorAll('.datepicker');\r\n    var instance = M.Datepicker.init(elems, {});\r\n    var elems = document.querySelectorAll('.dropdown-trigger');\r\n    var instances = M.Dropdown.init(elems, {});\r\n}\r\nexports.initDashboard = initDashboard;\r\n\n\n//# sourceURL=webpack:///./scripts/base.ts?");

/***/ }),

/***/ "./scripts/controllers/dispatcher/dispatcher.ts":
/*!******************************************************!*\
  !*** ./scripts/controllers/dispatcher/dispatcher.ts ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\r\n/// <reference path=\"../../../typings/global.d.ts\" />\r\nObject.defineProperty(exports, \"__esModule\", { value: true });\r\nvar DispatcherController = /** @class */ (function () {\r\n    function DispatcherController() {\r\n    }\r\n    DispatcherController.prototype.handleLogic = function () {\r\n        if (document.querySelectorAll(\".datatable\").length > 0 &&\r\n            document.querySelectorAll(\".datatable2\").length > 0) {\r\n            var dataTable = new DataTable(\".datatable\", {\r\n                perPage: 10,\r\n            });\r\n            var dataTable = new DataTable(\".datatable2\", {\r\n                perPage: 10,\r\n            });\r\n        }\r\n        // var dataTable = new DataTable(\".datatable3\",{\r\n        // \tperPage:10\r\n        // });\r\n        // var dataTable = new DataTable(\".datatable4\",{\r\n        // \tperPage:10\r\n        // });\r\n        // init calendar\r\n        var calendarEl = document.getElementById(\"calendar\");\r\n        if (calendarEl != undefined) {\r\n            var calendar = new FullCalendar.Calendar(calendarEl, {\r\n                plugins: ['dayGrid', 'googleCalendar'],\r\n                googleCalendarApiKey: \"AIzaSyDzWcZv7q04t-8hbr2TkbKr-XFdKBJbMAs\",\r\n                events: {\r\n                    googleCalendarId: \"od9mode2m7q35qqi7u968pdfuk@group.calendar.google.com\",\r\n                },\r\n            });\r\n            calendar.render();\r\n        }\r\n    };\r\n    return DispatcherController;\r\n}());\r\nexports.default = DispatcherController;\r\n\n\n//# sourceURL=webpack:///./scripts/controllers/dispatcher/dispatcher.ts?");

/***/ }),

/***/ "./scripts/controllers/driver/driver.ts":
/*!**********************************************!*\
  !*** ./scripts/controllers/driver/driver.ts ***!
  \**********************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\r\nObject.defineProperty(exports, \"__esModule\", { value: true });\r\nvar DriverController = /** @class */ (function () {\r\n    function DriverController() {\r\n    }\r\n    DriverController.prototype.handleLogic = function () {\r\n        console.log(\"driving!\");\r\n    };\r\n    return DriverController;\r\n}());\r\nexports.default = DriverController;\r\n\n\n//# sourceURL=webpack:///./scripts/controllers/driver/driver.ts?");

/***/ })

/******/ });