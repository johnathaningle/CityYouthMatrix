
export namespace M {
    export class Sidenav {
        static init(nodes: NodeListOf<Element>, options: any): Sidenav
    }
    export class Tabs {
        static init(nodes: NodeListOf<Element>, options: any): Tabs
    }
}

export class DataTable {
    constructor(selector: string, options: any)
}

export namespace FullCalendar {
    export class Calendar {
        constructor(element: HTMLElement, options: Partial<CalendarOptions>)
        render(): void
    }
    export interface CalendarOptions {
        plugins: Array<string>
    }
}
