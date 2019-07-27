import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { AuthService } from '../../service/auth.service';
import { Subscription } from 'rxjs';
import { MatSnackBar } from '@angular/material';


@Component({
    selector: 'app-auth',
    templateUrl: './auth.component.html',
    styleUrls: ['./auth.component.scss']
})
export class AuthComponent implements OnInit {

    hide = true;

    loginForm = this.fb.group({
        'login': ['', [Validators.required, Validators.minLength(3)]],
        'password': ['', [Validators.required, Validators.minLength(6)]],
    });

    registerForm = this.fb.group({
        'login': ['', [Validators.required, Validators.minLength(3)]],
        'password': ['', [Validators.required, Validators.minLength(6)]],
    });

    registerSubscription: Subscription;
    loginSubscription: Subscription;

    snackTime = 3500;
    action = 'close'

    constructor(
        private fb: FormBuilder,
        private auth: AuthService,
        private snackBar: MatSnackBar
    ) { }

    ngOnInit() {
        this.registerSubscription = new Subscription();
        this.loginSubscription = new Subscription();
    }

    submitRegisterForm() {
        if (!this.registerForm.valid) return;
        this.registerSubscription = this.auth.registerUser(this.registerForm.value).subscribe(
            data => {
                localStorage.setItem('token', data['token']),
                localStorage.setItem('name', data['name']),
                this.snackBar.open('Successfully registered', this.action, { duration: this.snackTime });
            },
            error => {
                this.snackBar.open(error.error['msg'], this.action, { duration: this.snackTime });
            },
        );
    }

    submitLoginForm() {
        if (!this.loginForm.valid) return;
        this.loginSubscription = this.auth.loginUser(this.registerForm.value).subscribe(
            data => {
                localStorage.setItem('token', data['token']);
                localStorage.setItem('name', data['name']),
                this.snackBar.open('Successfully logged', this.action, { duration: this.snackTime });
            },
            error => {
                this.snackBar.open(error.error['msg'], this.action, { duration: this.snackTime });
            },
        );
    }

    ngOnDestroy() {
        this.registerSubscription.unsubscribe();
        this.loginSubscription.unsubscribe();
    }
}
