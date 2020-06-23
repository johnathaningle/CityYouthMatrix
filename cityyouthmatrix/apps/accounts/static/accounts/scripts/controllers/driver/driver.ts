/// <reference path="../../../typings/global.d.ts" />

import * as $ from "jquery";

export default class DriverController implements IController {
    handleLogic(): void {
        $.getJSON("/api/getdrivercontext").then((response: DTO.DriverContext, status) => {

            if(status == "success") {
                var managedTrips = $("#manage-trips")
                var managedMarkup = ""
                response.managed_trips.forEach(x => {
                    managedMarkup += `<tr>
                        <td>${x.date}</td>
                        <td>${x.time}</td>
                        <td>${x.family}</td>
                        <td>NA</td>
                        <td>${x.pickup_address}</td>
                        <td>${x.dropoff_addresss}</td>
                        <td>${x.contact_number}</td>
                        <td><i class="material-icons">check</i></td>
                        <td><a href="tripinfo"><i class="material-icons">edit</i></a></td>
                      </tr>`
                })
                managedTrips.html(managedMarkup);
                managedMarkup = ""
                response.unassigned_trips.forEach(x => {
                    managedMarkup += `<tr>
                        <td>${x.date}</td>
                        <td>${x.time}</td>
                        <td>${x.family}</td>
                        <td>NA</td>
                        <td>${x.pickup_address}</td>
                        <td>${x.dropoff_addresss}</td>
                        <td>${x.contact_number}</td>
                        <td><i class="material-icons">check</i></td>
                        <td><a href="tripinfo"><i class="material-icons">edit</i></a></td>
                      </tr>`
                })
                var unmanagedTrips = $("#unassigned-trips")
                unmanagedTrips.html(managedMarkup);
            }
        });

    }

}