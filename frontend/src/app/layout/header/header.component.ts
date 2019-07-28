import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router } from '@angular/router';

import { AppService } from '../../service/app.service'
import { AuthService } from '../../service/auth.service';
import { Subscription } from 'rxjs';

@Component({
    selector: 'app-header',
    templateUrl: './header.component.html',
    styleUrls: ['./header.component.scss']
})
export class AppHeaderComponent implements OnInit, OnDestroy {

    logoutSubscriber: Subscription;
    routes = {
        mainPage: '/',
        profile: '/profile',
        login: '/login',
    }

    constructor(
        private appService: AppService,
        private router: Router,
        private auth: AuthService,
    ) {
        this.logoutSubscriber = new Subscription();
    }

    redirectMainPage() {
        this.router.navigate([this.routes.mainPage]);
    }

    redirectProfilePage() {
        this.router.navigate([this.routes.profile]);
    }

    redirectLoginPage() {
        this.router.navigate([this.routes.login]);
    }

    logout() {
        this.auth.logoutUser().subscribe(
            data => {
                localStorage.removeItem('token');
                localStorage.removeItem('name');
                this.auth.loggedUserName = null;
                this.router.navigate(['/tournaments']);
            }
        );
    }

    ngOnInit() {
    }

    ngOnDestroy() {
        this.logoutSubscriber.unsubscribe();
    }

}
