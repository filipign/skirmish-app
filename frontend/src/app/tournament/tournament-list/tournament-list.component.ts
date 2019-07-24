import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { DataSource } from '@angular/cdk/table';

import { TournamentService } from '../../service/tournament.service';
import { TournamentList } from '../../service/tournament.interface';
import { MatTableDataSource } from '@angular/material';

@Component({
    selector: 'app-tournament-list',
    templateUrl: './tournament-list.component.html',
    styleUrls: ['./tournament-list.component.scss']
})
export class TournamentListComponent implements OnInit, OnDestroy {

    tournamentList: MatTableDataSource<TournamentList>;
    tournamentSubscriber: Subscription;

    displayedColumns: string[] = ['name', 'date', 'participants', 'actions'];

    constructor(private tournament: TournamentService) { }

    ngOnInit() {
        this.tournamentSubscriber = this.tournament.getTournaments().subscribe(
            data => {
                this.tournamentList = new MatTableDataSource(data)
            }
        );
    }

    ngOnDestroy() {
        this.tournamentSubscriber.unsubscribe();
    }

}
