import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '../../environments/environment';
import { TournamentList, TournamentCreator } from './tournament.interface';
import { getTokenHeaders } from '../service/auth.interface';

@Injectable({
    providedIn: 'root',
})
export class TournamentService {

    private routes = {
        tournament: `${environment.backendUrl}/tournament`
    }

    constructor(private httpClient: HttpClient) { }

    getTournaments() {
        return this.httpClient.get<TournamentList[]>(this.routes.tournament);
    }

    createTournament(tournamentData: TournamentCreator) {
        return this.httpClient.post(
            this.routes.tournament,
            tournamentData,
            {
                headers: getTokenHeaders()
            }
        );
    }
}
