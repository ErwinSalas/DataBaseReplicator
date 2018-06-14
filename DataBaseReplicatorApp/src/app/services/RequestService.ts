import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
/**
 * Class to conect with back end, this container the method GET, POST, PUT and DELETE.
 *
 * @export
 * @class RequestService
 */
@Injectable()
export class RequestService {

   /* private addressServer = 'http://172.24.116.109:8000/api/'; // Ruta con XAMMP activo.
    private addressServerPost = 'http://172.24.116.109:8000/api/'; // Ruta por el archivo web.php en el servidor.
    private apiRoot = 'http://172.24.116.109:8000/api/'; // Ruta por el archivo api.php en el servidor.
    */
private addressServer = 'http://localhost:8000/api/'; // Ruta con XAMMP activo.
private addressServerPost = 'http://localhost:8000/api/'; // Ruta por el archivo web.php en el servidor.
private apiRoot = 'http://localhost:8000/api/'; // Ruta por el archivo api.php en el servidor.


// Las cabeceras necesarias para las peticiones http.
    private headers = {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
    };

    constructor(private http: HttpClient) {}

    /**
     * Call the server with get method.
     *
     * @param {string} url : endpoint => 'exampleUrl'
     * @param {string} params : "?param1=value&?param1=value... | '' | null
     * @param {class} context : The context of the development environment <=> this
     * @param {Function} callback : Where will return the data from backend
     * @memberof RequestService
     */
    getRequest(url, params, context, callback) {
        this.http
            .get(this.apiRoot + url + params)
            .subscribe((res: any) => callback(context, res));
    }

    getRequestHola(url: string) {
        const req = new XMLHttpRequest();
        req.open('get', this.apiRoot + url, false);
        req.send(null);
        return req.responseText;
    }

    /**
     * Insert element in the backend, you can sent all properities by JSON.
     *
     * @param {string} url : endpoint => 'exampleUrl'
     * @param {JSON} data : {data: value, data: value} | {}
     * @param {class} context : The context of the development environment <=> this
     * @param {Function} callback : Where will return the data, success
     * @memberof RequestService
     */
    postRequest(url, data, context, callback) {
        let params = 'json=' + JSON.stringify(data); // El backend recogerá un parametro json
        this.http
            .post(this.apiRoot + url, params, this.headers)
            .subscribe((res: any) => callback(context, res));
    }

    // TODO: Add the context in the method, find other way of do.
    /**
     * Update element, you cant send by body all properties to update.
     *
     * @param {string} url : endpoint => 'exampleUrl'
     * @param {JSON} data : {data: value, data: value} | {}
     * @param {class} context : The context of the development environment <=> this
     * @param {Function} callback : Where will return the data, success
     * @memberof RequestService
     */
    putRequest(url, data, context, callback) {
        let params = 'json=' + JSON.stringify(data); // El backend recogerá un parametro json
        this.http
            .put(this.apiRoot + url, params, this.headers)
            .subscribe((res: any) => callback(context, res));
    }

    /**
     * Delete a element in the back-end by id.
     *
     * @param {string} url : endpoint => 'exampleUrl'
     * @param {any} id : ?param1=value&?param1=value... |
     * @param {class} context : The context of the development environment <=> this
     * @param {Function} callback : Where will return the data, success
     * @memberof RequestService
     */
    deleteRequest(url, id, context, callback) {
        this.http
            .delete(this.apiRoot + url + id, this.headers)
            .subscribe((res: any) => callback(context, res));
    }
}