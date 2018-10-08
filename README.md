# NBAsy

NBAsy is a lighweight package for retrieving player and team stats from stats.nba.com.

  - Get sorted player lists and season stats
  - Player box scores (TODO)

### Installation

(TODO) This package has not been uploaded to pip yet.  Download this repository to use.

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

        'GP': 72,                   # Games played
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
        'DREB_RANK': 54,            # Defensive rebounds rank
        'FG_PCT_RANK': 244,         # Field goal percentage rank
        'FG3_PCT_RANK': 169,        # 3 point field goal percentage rank
        'FG3A_RANK': 1,             # 3 point shots attempted rank
        'FG3M_RANK': 2,             # 3 point field goals made rank
        'FGA_RANK': 2,              # Field goals attempted rank
        'FGM_RANK': 7,              # Field goals made rank
        'FT_PCT_RANK': 78,          # Free throw percentage rank
        'FTA_RANK': 1,              # Free throws attempted rank
        'FTM_RANK': 1,              # Free throws made rank
        'GP_RANK': 154,             # Games played rank
        'L_RANK': 386,              # Game losses rank
        'MIN_RANK': 15,             # Minutes rank
        'NBA_FANTASY_PTS_RANK': 5,  # NBA fantasy points rank
        'OREB_RANK': 259,           # Offensive rebounds rank
        'PF_RANK': 92,              # Personal fouls rank
        'PFD_RANK': 3,              # Personal fouls drawn rank
        'PLUS_MINUS_RANK': 7,       # Plus minus rank
        'PTS_RANK': 1,              # Points / game rank
        'REB_RANK': 85,             # Rebounds rank
        'STL_RANK': 9,              # Steals rank
        'TD3_RANK': 5,              # Triple doubles rank
        'TOV_RANK': 3,              # Turnovers rank
        'W_PCT_RANK': 17,           # Win percentage rank
        'W_RANK': 3,                # Wins rank


        # Team Details

        'TEAM_ABBREVIATION': 'HOU', # 3 letter team code
        'TEAM_ID': 1610612745,      # NBA api team id

        # Player

        'AGE': 28.0,                # Player age
        'PLAYER_ID': 201935,        # NBA api player id

        # Games



        'L': 13,
        'FG3M': 3.7,

        'BLKA': 1.4,
        'CFID': 5,
        'FG3_PCT': 0.367,


        'PLUS_MINUS': 7.3,


        'W_PCT': 0.819,

        'DD2': 31,


        'PFD': 7.0,

        'W': 59,
        'PF': 2.3,
        'FG3A': 10.0,
        'TD3': 4,
    }
)])
```