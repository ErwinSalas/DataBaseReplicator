import { Schema } from './Schema';

export class DataBase {
    name: String;
    size: String;
    schemas: Array<Schema>;

    constructor(
        name: String,
        size: String,
        schemas: Array<Schema>
      ) {
        this.name = name;
        this.size = size;
        this.schemas = schemas;
    }

}
