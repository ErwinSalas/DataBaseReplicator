export class DataBaseConfig {
    host: String;
    pasword: String;
    name: String;
    port: String;


    constructor(
        host: String,
        pasword: String,
        name: String,
        port: String,

    ) {
        this.host = host;
        this.pasword = pasword;
        this.name = name;
        this.port = port;

    }

}
