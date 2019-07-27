import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { TournamentListComponent } from './tournament/tournament-list/tournament-list.component';
import { AuthComponent } from './auth/auth/auth.component';
import { ProfileComponent } from './profile/profile.component';

const routes: Routes = [
    { path: 'tournaments', component: TournamentListComponent },
    { path: 'profile', component: ProfileComponent },
    { path: 'login', component: AuthComponent },
    { path: '**', component: TournamentListComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
