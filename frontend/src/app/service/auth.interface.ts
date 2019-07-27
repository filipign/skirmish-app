import { HttpHeaders } from '@angular/common/http';

export interface UserRegister {
    login: string,
    password: string,
}

export interface UserProfile {
    name: string,
    date_created: string,
}

export function getTokenHeaders() {
    return new HttpHeaders({
        'Content-Type': 'application/json',
        'token': localStorage.getItem('token'),
    });
}