import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '../../environments/environment';
import { TournamentList } from './tournament.interface';

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
}
