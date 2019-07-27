import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '../../environments/environment';
import { UserRegister } from './auth.interface';

@Injectable({
    providedIn: 'root',
})
export class AuthService {

    private routes = {
        register: `${environment.backendUrl}/auth/register`,
        login: `${environment.backendUrl}/auth/login`,
    }

    constructor(private httpClient: HttpClient) { }

    registerUser(userData: UserRegister) {
        return this.httpClient.post(this.routes.register, userData);
    }

    loginUser(userData: UserRegister) {
        return this.httpClient.post(this.routes.login, userData);
    }
}
