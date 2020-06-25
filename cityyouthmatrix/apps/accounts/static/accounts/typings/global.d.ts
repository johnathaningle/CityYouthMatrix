
declare namespace M {
    class Sidenav {
        static init(nodes: NodeListOf<Element>, options: any): Sidenav
    }
    class Tabs {
        static init(nodes: NodeListOf<Element>, options: any): Tabs
    }
    class Collapsible {
        static init(nodes: NodeListOf<Element>, options: any): Collapsible
    }

    class Dropdown {
        static init(nodes: NodeListOf<Element>, options: any): Dropdown
    }

    class FormSelect {
        static init(nodes: NodeListOf<Element>, options: any): FormSelect
    }

    class Datepicker {
        static init(nodes: NodeListOf<Element>, options: any): Datepicker
    }

    class Timepicker {
        static init(nodes: NodeListOf<Element>, options: any): Timepicker
    }

    class Modal {
        static init(nodes: NodeListOf<Element>, options: any): Modal
    }
}


declare class DataTable {
    constructor(selector: string, options: any)
}

declare namespace FullCalendar {
    class Calendar {
        constructor(element: HTMLElement, options: Partial<CalendarOptions>)
        render(): void
    }
    interface CalendarOptions {
        plugins: Array<string>
        googleCalendarApiKey: string
        events: any
    }
}

declare interface IController {
    handleLogic(): void
}

declare namespace DTO {
    export interface SerializedTrip {
        date: string
        time: string
        family: string
        num_adults: number
        num_kids: number
        pickup_address: string
        dropoff_addresss: string
        contact_number: string
        is_returned: boolean
    }

    export interface DriverContext {
        managed_trips: Array<SerializedTrip>
        unassigned_trips: Array<SerializedTrip>
    }
}



