import { Component, OnInit } from '@angular/core';

import { AppService } from '../../service/app.service'

@Component({
    selector: 'app-header',
    templateUrl: './header.component.html',
    styleUrls: ['./header.component.scss']
})
export class AppHeaderComponent implements OnInit {

    name: string;

    constructor(private appService: AppService) {
        this.name = localStorage.getItem('name')
    }

    ngOnInit() {
    }

}
