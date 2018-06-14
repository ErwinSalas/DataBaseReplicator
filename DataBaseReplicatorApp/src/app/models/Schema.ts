export class Schema {
    name: String;
    tables: Array<string>;


    constructor(
        name: String,
        tables: Array<string>
    ) {
        this.name = name;
        this.tables = tables;
    }
}
