export interface Tournament {
    name: string,
    date: string,
    participants: number,
    uuid: string,
}

export interface TournamentList extends Array<Tournament>{};