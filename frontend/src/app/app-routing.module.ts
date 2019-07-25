import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { TournamentListComponent } from './tournament/tournament-list/tournament-list.component';
import { AuthComponent } from './auth/auth/auth.component';

const routes: Routes = [
    { path: 'tournaments', component: TournamentListComponent },
    { path: 'login', component: AuthComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
