# NBAsy

NBAsy is a lighweight package for retrieving player and team stats from stats.nba.com.

  - Get sorted player lists and season stats
  - Player box scores (TODO)

### Installation

NBAsy may work on Python 2 but Python 3 is recommended.

To install:

```sh
$ pip install nbasy
```

### Usage

#### Import the player list class

```python
from nbasy.player_lists import PlayerList
```

#### Get the player list

```python
player_list = PlayerList().get_player_list()
```

This will return an ordered dict of all players and their stats for a season (default ordering is by PTS/Game).
Good practice is to specify the season you want data from.  This can be done with the following:

```python
player_list = PlayerList(season='2017-18').get_player_list()
```

Thats it! Take the returned dict of data and do with it what you please. The player list is returned in the following format:

```python
>>> PlayerList(season='2017-18', players=["James Harden"]).get_player_list()
OrderedDict([(
    'James Harden', {

        # Main/Common Stats

        'MIN': 35.4,                # Minutes / game

        'PTS': 30.4,                # Points/game
        'AST': 8.8,                 # Assists / game

        'REB': 5.4,                 # Rebound / game
        'DREB': 4.8,                # Defensive rebounds / game
        'OREB': 0.6,                # Offensive rebounds / game

        'STL': 1.8,                 # Steals / game
        'BLK': 0.7,                 # Blocks / game

        'FGM': 9.0,                 # Field goals made / game
        'FGA': 20.1,                # Field goals attempted / game
        'FG_PCT': 0.449,            # Field goal percentage

        'FTM': 8.7,                 # Free throws made / game
        'FTA': 10.1,                # Free throws attempted / game
        'FT_PCT': 0.858,            # Free throw percentage

        'TOV': 4.4,                 # Turnovers / game

        'NBA_FANTASY_PTS': 53.0     # Fantasy points / game


        # Ranks
        'AST_RANK': 4,              # Assists rank
        'BLK_RANK': 84,             # Blocks rank
        'BLKA_RANK': 3,             # Blocks against rank
        'DD2_RANK': 15,             # Double doubles rank

        'FG3A_RANK': 1,             # 3 point shots attempted rank
        'GP_RANK': 154,             # Games played rank

        'L_RANK': 386,              # Game losses rank
        'STL_RANK': 9,              # Steals rank

        'OREB_RANK': 259,           # Offensive rebounds rank
        'FGM_RANK': 7,              # Field goals made rank
        'PFD_RANK': 3,              # Personal fouls drawn rank



        'MIN_RANK': 15,             # Minutes rank
        'TD3_RANK': 5,
        'TOV_RANK': 3,
        'PTS_RANK': 1,
        'PLUS_MINUS_RANK': 7,
        'FG3M_RANK': 2,
        'DREB_RANK': 54,
        'FTA_RANK': 1,
        'W_PCT_RANK': 17,

        'FG_PCT_RANK': 244,

        'FG3_PCT_RANK': 169,
        'FT_PCT_RANK': 78,
        'NBA_FANTASY_PTS_RANK': 5,
        'PF_RANK': 92,
        'FTM_RANK': 1,
        'FGA_RANK': 2,
        'W_RANK': 3,
        'REB_RANK': 85,



        'TEAM_ID': 1610612745,
        'L': 13,
        'FG3M': 3.7,
        'PLAYER_ID': 201935,
        'BLKA': 1.4,
        'CFID': 5,
        'FG3_PCT': 0.367,

        'TEAM_ABBREVIATION': 'HOU',
        'PLUS_MINUS': 7.3,


        'W_PCT': 0.819,

        'DD2': 31,


        'PFD': 7.0,

        'W': 59,
        'GP': 72,

        'AGE': 28.0,

        'PF': 2.3,

        'FG3A': 10.0,
        'STL': 1.8,

        'TD3': 4,
    }
)])
```