import { Tables } from './Tables';
export class Schema {
    name: String;
    tables: Array<Tables>;


    constructor(
        name: String,
        tables: Array<Tables>
    ) {
        this.name = name;
        this.tables = tables;
    } 
}
