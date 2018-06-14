import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClient } from '@angular/common/http'; // For conection with server.

import {NgbModule} from '@ng-bootstrap/ng-bootstrap';

import { SideBarComponent } from '../components/side-bar/side-bar.component';
import { CreateConnectionComponent } from '../components/create-connection/create-connection.component';
import { MainComponent } from './main.component';
import { CommonModule } from '@angular/common';

@NgModule({
  imports: [
    CommonModule, SideBarComponent,
    CreateConnectionComponent,
    HttpClientModule
  ],
  declarations: [MainComponent]
})
export class MainModule { }
