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
>>> PlayerList(season='2017-18', players=["James Harden"])
OrderedDict([(
    'James Harden', {
        'L_RANK': 386,
        'TEAM_ID': 1610612745,
        'L': 13,
        'STL_RANK': 9,
        'BLK_RANK': 84,
        'CFPARAMS': '201935,1610612745',
        'FT_PCT': 0.858,
        'FG3M': 3.7,
        'PLAYER_ID': 201935,
        'AST': 8.8,
        'OREB_RANK': 259,
        'BLK': 0.7,
        'FGM_RANK': 7,
        'PFD_RANK': 3,
        'BLKA': 1.4,
        'CFID': 5,
        'BLKA_RANK': 3,
        'FG3A_RANK': 1,
        'AST_RANK': 4,
        'MIN_RANK': 15,
        'DREB': 4.8,
        'FGA': 20.1,
        'DD2_RANK': 15,
        'FG3_PCT': 0.367,
        'TD3_RANK': 5,
        'TOV_RANK': 3,
        'PTS_RANK': 1,
        'FG_PCT_RANK': 244,
        'TEAM_ABBREVIATION': 'HOU',
        'PLUS_MINUS': 7.3,
        'FGM': 9.0,
        'PLUS_MINUS_RANK': 7,
        'FG3M_RANK': 2,
        'MIN': 35.4,
        'DREB_RANK': 54,
        'W_PCT': 0.819,
        'FG3_PCT_RANK': 169,
        'DD2': 31,
        'FTA_RANK': 1,
        'PTS': 30.4,
        'OREB': 0.6,
        'FTA': 10.1,
        'PFD': 7.0,
        'FTM': 8.7,
        'W': 59,
        'GP': 72,
        'W_PCT_RANK': 17,
        'TOV': 4.4,
        'FG_PCT': 0.449,
        'GP_RANK': 154,
        'AGE': 28.0,
        'REB': 5.4,
        'FT_PCT_RANK': 78,
        'PF': 2.3,
        'NBA_FANTASY_PTS_RANK': 5,
        'PF_RANK': 92,
        'FTM_RANK': 1,
        'FG3A': 10.0,
        'STL': 1.8,
        'FGA_RANK': 2,
        'W_RANK': 3,
        'TD3': 4,
        'REB_RANK': 85,
        'NBA_FANTASY_PTS': 53.0
    }
)])
```