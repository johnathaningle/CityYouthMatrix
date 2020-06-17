
declare namespace M {
    class Sidenav {
        static init(nodes: NodeListOf<Element>, options: any): Sidenav
    }
    class Tabs {
        static init(nodes: NodeListOf<Element>, options: any): Tabs
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
    }
}



