import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { FlexLayoutModule } from '@angular/flex-layout';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import {
    MatButtonModule,
    MatCheckboxModule,
    MatToolbarModule,
    MatMenuModule,
    MatTableModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatIconModule,
    MatSnackBarModule,
} from '@angular/material';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AppHeaderComponent } from './layout/header/header.component';
import { TournamentListComponent } from './tournament/tournament-list/tournament-list.component';
import { AuthComponent } from './auth/auth/auth.component';
import { ProfileComponent } from './profile/profile.component';
import { EditorComponent } from './tournament/editor/editor.component';
import { TournamentComponent } from './tournament/tournament/tournament.component';

@NgModule({
    declarations: [
        AppComponent,
        AppHeaderComponent,
        TournamentListComponent,
        AuthComponent,
        ProfileComponent,
        EditorComponent,
        TournamentComponent,
    ],
    imports: [
        FormsModule,
        ReactiveFormsModule,
        BrowserAnimationsModule,
        FlexLayoutModule,
        BrowserModule,
        AppRoutingModule,
        MatButtonModule,
        MatCheckboxModule,
        MatToolbarModule,
        MatMenuModule,
        HttpClientModule,
        MatTableModule,
        MatCardModule,
        MatFormFieldModule,
        MatInputModule,
        MatIconModule,
        MatSnackBarModule,
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule { }
