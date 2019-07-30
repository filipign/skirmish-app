import { Component, OnInit, OnDestroy } from '@angular/core';

import { AuthService } from '../service/auth.service';
import { UserProfile } from '../service/auth.interface';
import { Subscription } from 'rxjs';

@Component({
    selector: 'app-profile',
    templateUrl: './profile.component.html',
    styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit, OnDestroy {

    userProfile: UserProfile;
    userSubscriber: Subscription;
    isLoaded = false;

    constructor(private auth: AuthService) { }

    ngOnInit() {
        this.userSubscriber = this.auth.getUserInfo().subscribe(
            data => {
                this.userProfile = data;
                this.isLoaded = true;
            },
        );
    }

    ngOnDestroy() {
        this.userSubscriber.unsubscribe();
    }
}
