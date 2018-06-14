import { Component, OnInit } from '@angular/core';
import { RequestService } from '../../services/RequestService';

@Component({
  selector: 'app-side-bar',
  providers: [RequestService],
  templateUrl: './side-bar.component.html',
  styleUrls: ['./side-bar.component.css']
})
export class SideBarComponent implements OnInit {
  requestService: any;

  constructor( requestService: RequestService) { }

  ngOnInit() {
    this.getRequest();
  }
  getRequest() {
    this.requestService.getRequest(
        'getDatabase',
        '',
        this,
        (context, res) => {
            context.JsonList = res;
            console.log(context.JsonList);
           // context.ParsingJsonToArray();
        }
    );
  }

}

