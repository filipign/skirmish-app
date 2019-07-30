import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';

import { TournamentService } from '../../service/tournament.service';
import { TournamentList } from '../../service/tournament.interface';
import { MatTableDataSource } from '@angular/material';
import { AuthService } from '../../service/auth.service';
import { Router } from '@angular/router';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
    selector: 'app-tournament-list',
    templateUrl: './tournament-list.component.html',
    styleUrls: ['./tournament-list.component.scss']
})
export class TournamentListComponent implements OnInit, OnDestroy {

    tournamentList: MatTableDataSource<TournamentList>;
    tournamentSubscriber: Subscription;
    creatorSubscriber: Subscription;

    openCreator = false;
    creatorForm = this.fb.group({
        'name': ['', [Validators.required, Validators.minLength(3)]],
    });

    routes = {
        login: '/login',
        tournament: `/tournament`
    }

    displayedColumns: string[] = ['name', 'date', 'participants', 'actions'];

    constructor(
        private tournament: TournamentService,
        private auth: AuthService,
        private router: Router,
        private fb: FormBuilder,
    ) { }

    ngOnInit() {
        this.tournamentSubscriber = this.tournament.getTournaments().subscribe(
            data => {
                this.tournamentList = new MatTableDataSource(data)
            }
        );
        this.creatorSubscriber = new Subscription();
    }

    ngOnDestroy() {
        this.tournamentSubscriber.unsubscribe();
        this.creatorSubscriber.unsubscribe();
    }

    redirectLoginPage() {
        this.router.navigate([this.routes.login]);
    }

    submitTournamentForm() {
        if (!this.creatorForm.valid) return;
        this.creatorSubscriber = this.tournament.createTournament(this.creatorForm.value).subscribe(
            data => {
                let uuid = data['uuid'];
                this.router.navigate([`/${this.routes.tournament}/${uuid}/edit`]);
            }
        )
    }

    navigate(row) {
        this.router.navigate([`/${this.routes.tournament}/${row.uuid}/edit`]);
    }
}
