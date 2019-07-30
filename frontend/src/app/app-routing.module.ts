import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { TournamentListComponent } from './tournament/tournament-list/tournament-list.component';
import { AuthComponent } from './auth/auth/auth.component';
import { ProfileComponent } from './profile/profile.component';
import { EditorComponent } from './tournament/editor/editor.component';
import { TournamentComponent } from './tournament/tournament/tournament.component';

const routes: Routes = [
    { path: 'tournament/:id/edit', component: EditorComponent },
    { path: 'tournament/:id', component: TournamentComponent },
    { path: 'tournament', component: TournamentListComponent },
    { path: 'profile', component: ProfileComponent },
    { path: 'login', component: AuthComponent },
    { path: '**', component: TournamentListComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
