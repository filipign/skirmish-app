import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '../../environments/environment';
import { UserRegister, UserProfile, getTokenHeaders } from './auth.interface';

@Injectable({
    providedIn: 'root',
})
export class AuthService {

    private routes = {
        register: `${environment.backendUrl}/auth/register`,
        login: `${environment.backendUrl}/auth/login`,
        info: `${environment.backendUrl}/auth/user`,
        logout: `${environment.backendUrl}/auth/logout`,
    }

    loggedUserName: string = null;

    constructor(private httpClient: HttpClient) { }

    registerUser(userData: UserRegister) {
        return this.httpClient.post(this.routes.register, userData);
    }

    loginUser(userData: UserRegister) {
        return this.httpClient.post(this.routes.login, userData);
    }

    getUserInfo() {
        return this.httpClient.get<UserProfile>(this.routes.info, {
            headers: getTokenHeaders(),
        });
    }

    logoutUser() {
        return this.httpClient.post(this.routes.logout, {
            headers: getTokenHeaders(),
        });
    }
}