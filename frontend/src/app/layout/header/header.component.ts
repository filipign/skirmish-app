import { Component, OnInit } from '@angular/core';

import { AppService } from '../../service/app.service'
import { Router } from '@angular/router';

@Component({
    selector: 'app-header',
    templateUrl: './header.component.html',
    styleUrls: ['./header.component.scss']
})
export class AppHeaderComponent implements OnInit {

    name: string;

    constructor(private appService: AppService, private router: Router) {
        this.name = localStorage.getItem('name')
    }

    redirectMainPage() {
        this.router.navigate(['/tournaments']);
    }

    redirectProfilePage() {
        this.router.navigate(['/profile']);
    }

    ngOnInit() {
    }

}
