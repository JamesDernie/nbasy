import nbasy.settings as settings
from collections import OrderedDict
from nbasy.utils import _get_json


class PlayerList:

    _endpoint = "leaguedashplayerstats"

    def __init__(self,
                 teams=None,  # Pass a list of teams,
                 players=None,  # Pass a list of players
                 player_position=settings.PlayerPosition.Default,
                 league_id=settings.NBA_LEAGUE_ID,
                 per_mode=settings.PerMode.PerGame,
                 stat_category=settings.StatCategory.Default,
                 season=settings.CURRENT_SEASON,
                 season_type=settings.SeasonType.Default,
                 scope=settings.Scope.Default,
                 game_scope=settings.Game_Scope.Default,
                 player_experience=settings.PlayerExperience.Default,
                 starter_bench=settings.StarterBench.Default,
                 measure_type=settings.MeasureType.Default,
                 plus_minus=settings.PlusMinus.Default,
                 pace_adjust=settings.PaceAdjust.Default,
                 rank=settings.Rank.Default,
                 location=settings.Location.Default,
                 month=settings.Month.All,
                 season_segment=settings.SeasonSegment.Default,
                 date_from=settings.DateFrom.Default,
                 date_to=settings.DateTo.Default,
                 opponent_team_id=settings.OpponentTeamID.Default,
                 vs_conference=settings.VsConference.Default,
                 vs_division=settings.VsDivision.Default,
                 outcome=settings.Outcome.Default,
                 game_segment=settings.GameSegment.Default,
                 period=settings.Period.AllQuarters,
                 last_n_games=settings.LastNGames.Default,
                 sorter=settings.Sorter.Default):

        if teams:
            assert isinstance(teams, list), "teams must be a list type"

        if players:
            assert isinstance(players, list), "players must be a list type"

        # Request params
        self.params = {
            'LeagueID': league_id,
            'PlayerPosition': player_position,
            'PerMode': per_mode,
            'StatCategory': stat_category,
            'Season': season,
            'SeasonType': season_type,
            'Scope': scope,
            'GameScope': game_scope,
            'PlayerExperience': player_experience,
            'StarterBench': starter_bench,
            'MeasureType': measure_type,
            'PlusMinus': plus_minus,
            'PaceAdjust': pace_adjust,
            'Rank': rank,
            'Location': location,
            'Month': month,
            'SeasonSegment': season_segment,
            'DateFrom': date_from,
            'DateTo': date_to,
            'OpponentTeamID': opponent_team_id,
            'VsConference': vs_conference,
            'VsDivision': vs_division,
            'Outcome': outcome,
            'GameSegment': game_segment,
            'Period': period,
            'LastNGames': last_n_games,
        }

        # Filter Params
        self.teams = teams
        self.players = players
        self.sorter = sorter

    def get_player_list(self):

        # Get Data
        json = _get_json(
            endpoint=self._endpoint,
            params=self.params
        )

        return self.process_json(json)

    def convert_to_dict(self, headers, player_list):
        """
        Converts the return results rowSet to a readable ordered dict
        Format:

            [(
                player_name: {
                    attr: value,
                    attr: value,
                    ...
                }
            )...]
        """

        # Get player name index in headers and remove from headers
        i = headers.index("PLAYER_NAME")
        headers.pop(i)

        # Sort player list
        sorter_index_key = headers.index(self.sorter)  # Need to know which item in list we want to sort by
        sorted_player_list = sorted(player_list, key=lambda x: x[sorter_index_key], reverse=True)

        player_dict = OrderedDict()
        for player in sorted_player_list:

            # Get player name for key
            player_name = player.pop(i)

            # Create key dict value
            player_data = {}
            for k, v in enumerate(player):
                player_data[headers[k]] = v

            player_dict[player_name] = player_data

        return player_dict

    def process_json(self, json):
        """
        Filter the data if player or team specified
        Process filtered data into a dictionary, with the player name as the dict key
        """

        headers = json["resultSets"][0]["headers"]
        player_list = json['resultSets'][0]['rowSet']

        # Filter by team if team
        if self.teams:

            # Get index of 'TEAM_ABBREVIATION' in headers
            i = headers.index('TEAM_ABBREVIATION')

            # Filter player list based on list of teams provided
            player_list = [player for player in player_list if player[i] in self.teams]

        # Filter by player name
        if self.players:

            # Get index of 'PLAYER_NAME' in headers
            i = headers.index('PLAYER_NAME')

            # Convert players to lowercase
            self.players = [x.lower() for x in self.players]

            # Filter player list based on list of teams provided
            player_list = [player for player in player_list if player[i].lower() in self.players]

        # Convert data to dict
        player_dict = self.convert_to_dict(headers, player_list)

        return player_dict
