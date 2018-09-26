from datetime import datetime


_curr_year = datetime.now().year
if datetime.now().month > 6:
    CURRENT_SEASON = str(_curr_year) + "-" + str(_curr_year + 1)[2:]
else:
    CURRENT_SEASON = str(_curr_year - 1) + "-" + str(_curr_year)[2:]


# League ID
NBA_LEAGUE_ID = '00'


TEAMS = {
    'ATL': {
        'city': 'Atlanta',
        'name': 'Hawks',
        'id': '1610612737',
    },
    'BOS': {
        'city': 'Boston',
        'name': 'Celtics',
        'id': '1610612738',
    },
    'BKN': {
        'city': 'Brooklyn',
        'name': 'Nets',
        'id': '1610612751',
    },
    'CHA': {
        'city': 'Charlotte',
        'name': 'Hornets',
        'id': '1610612766',
    },
    'CHI': {
        'city': 'Chicago',
        'name': 'Bulls',
        'id': '1610612741',
    },
    'CLE': {
        'city': 'Cleveland',
        'name': 'Cavaliers',
        'id': '1610612739',
    },
    'DAL': {
        'city': 'Dallas',
        'name': 'Mavericks',
        'id': '1610612742',
    },
    'DEN': {
        'city': 'Denver',
        'name': 'Nuggets',
        'id': '1610612743',
    },
    'DET': {
        'city': 'Detroit',
        'name': 'Pistons',
        'id': '1610612765',
    },
    'GSW': {
        'city': 'Golden State',
        'name': 'Warriors',
        'id': '1610612744',
    },
    'HOU': {
        'city': 'Houston',
        'name': 'Rockets',
        'id': '1610612745',
    },
    'IND': {
        'city': 'Indiana',
        'name': 'Pacers',
        'id': '1610612754',
    },
    'LAC': {
        'city': 'Los Angeles',
        'name': 'Clippers',
        'id': '1610612746',
    },
    'LAL': {
        'city': 'Los Angeles',
        'name': 'Lakers',
        'id': '1610612747',
    },
    'IND': {
        'city': 'Indiana',
        'name': 'Pacers',
        'id': '1610612754',
    },

}


class _DefaultN:
    Default = 'N'


class _DefaultBlank:
    Default = ''


class _DefaultZero:
    Default = '0'


class PerMode:
    Totals = 'Totals'
    PerGame = 'PerGame'
    MinutesPer = 'MinutesPer'
    Per48 = 'Per48'
    Per40 = 'Per40'
    Per36 = 'Per36'
    PerMinute = 'PerMinute'
    PerPossession = 'PerPossession'
    PerPlay = 'PerPlay'
    Per100Possessions = 'Per100Possessions'
    Per100Plays = 'Per100Plays'
    Default = PerGame


class SeasonType:
    Regular = 'Regular Season'
    Playoffs = 'Playoffs'
    Default = Regular


class StatCategory:
    PTS = 'PTS'
    FGM = 'FGM'
    FGA = 'FGA'
    FG_PCT = 'FG%'
    FG3M = '3PM'
    FG3A = '3PA'
    FG3_PCT = '3P%'
    FTM = 'FTM'
    FTA = 'FTA'
    FT_PCT = 'FT%'
    OREB = 'OREB'
    DREB = 'DREB'
    REB = 'REB'
    AST = 'AST'
    STL = 'STL'
    BLK = 'BLK'
    TOV = 'TOV'
    EFF = 'EFF'
    AST_TOV = 'AST/TO'
    STL_TOV = 'STL/TOV'
    PF = 'PF'
    Default = PTS


class Scope:
    AllPlayers = 'S'
    Rookies = 'Rookies'
    Default = AllPlayers


class MeasureType:
    Base = 'Base'
    Advanced = 'Advanced'
    Misc = 'Misc'
    FourFactors = 'Four Factors'
    Scoring = 'Scoring'
    Opponent = 'Opponent'
    Usage = 'Usage'
    Default = Base


class PtMeasureType:
    SpeedDistance = 'SpeedDistance'


class GroupQuantity:
    Default = 5


class Outcome(_DefaultBlank):
    Win = 'W'
    Loss = 'L'


class Location(_DefaultBlank):
    Home = 'Home'
    Away = 'Away'


class SeasonSegment(_DefaultBlank):
    EntireSeason = ''
    PreAllStar = 'Pre All-Star'
    PostAllStar = 'Post All-Star'


class DateFrom(_DefaultBlank):
    pass


class DateTo(_DefaultBlank):
    pass


class VsConference(_DefaultBlank):
    All = ''
    East = 'East'
    West = 'West'


class VsDivision(_DefaultBlank):
    All = ''
    Atlantic = 'Atlantic'
    Central = 'Central'
    Northwest = 'Northwest'
    Pacific = 'Pacific'
    Southeast = 'Southeast'
    Southwest = 'Southwest'


class GameSegment(_DefaultBlank):
    EntireGame = ''
    FirstHalf = 'First Half'
    SecondHalf = 'Second Half'
    Overtime = 'Overtime'


class ClutchTime(_DefaultBlank):
    Last5Min = 'Last 5 Minutes'
    Last4Min = 'Last 4 Minutes'
    Last3Min = 'Last 3 Minutes'
    Last2Min = 'Last 2 Minutes'
    Last1Min = 'Last 1 Minutes'
    Last30Sec = 'Last 30 Seconds'
    Last10Sec = 'Last 10 Seconds'


class ShotClockRange(_DefaultBlank):
    AllRanges = ''
    # I honestly don't know anytime the shot clock would be off
    ShotClockOff = 'ShotClock Off'

    def get(self, n):
        if n > 24 or n < 0:
            return ''
        elif 22 <= n <= 24:
            return '24-22'
        elif 18 <= n < 22:
            return '22-18 Very Early'
        elif 15 <= n < 18:
            return '18-15 Early'
        elif 7 <= n < 15:
            return '15-7 Average'
        elif 4 <= n < 7:
            return '7-4 Late'
        elif 0 <= n < 4:
            return '4-0 Very Late'


class AheadBehind(_DefaultBlank):
    AheadOrBehind = 'Ahead or Behind'
    AheadOrTied = 'Ahead or Tied'
    BehindOrTied = 'Behind or Tied'


class PlusMinus(_DefaultN):
    pass


class PaceAdjust(_DefaultN):
    pass


class Rank(_DefaultN):
    pass


class OpponentTeamID(_DefaultZero):
    pass


class Period(_DefaultZero):
    AllQuarters = '0'
    FirstQuarter = '1'
    SecondQuarter = '2'
    ThirdQuarter = '3'
    FourthQuarter = '4'

    def Overtime(self, n):
        return str(4 + n)


class LastNGames(_DefaultZero):
    pass


class PlayoffRound(_DefaultZero):
    All = '0'
    QuarterFinals = '1'
    SemiFinals = '2'
    ConferenceFinals = '3'
    Finals = '4'


class Month(_DefaultZero):
    All = '0'
    October = '1'
    November = '2'
    December = '3'
    January = '4'
    February = '5'
    March = '6'
    April = '7'
    May = '8'
    June = '9'
    July = '10'
    August = '11'
    September = '12'


class RangeType(_DefaultZero):
    pass


class StartRange(_DefaultZero):
    pass


class EndRange(_DefaultZero):
    pass


class StartPeriod(Period):
    pass


class EndPeriod(Period):
    pass


class ContextMeasure:
    # Not sure if this is mapped correctly. Source:
    # https://github.com/bradleyfay/NBAStats
    FGM = 'FGM'
    FGA = 'FGA'
    FG_PCT = 'FG_PCT'
    FG3M = 'FG3m'
    FG3A = 'FG3A'
    FG3_PCT = 'FG3_PCT'
    PF = 'PF'
    EFG_PCT = 'EFG_PCT'
    TS_PCT = 'TS_PCT'
    PTS_FB = 'PTS_FB'
    PTS_OFF_TOV = 'PTS_OFF_TOV'
    PTS_2ND_CHANCE = 'PTS_2ND_CHANCE'
    Default = FGM


class PlayerScope:
    AllPlayers = 'All Players'
    Rookies = 'Rookie'
    Default = AllPlayers


class PlayerOrTeam:
    Player = 'Player'
    Team = 'Team'
    Default = Player


class GameScope:
    Season = 'Season'
    Last10 = 'Last 10'
    Yesterday = 'Yesterday'
    Finals = 'Finals'
    Default = Season


class Game_Scope(_DefaultBlank):
    Last10 = 'Last 10'
    Yesterday = 'Yesterday'


class Conference(VsConference):
    pass


class Division(VsDivision):
    pass


class TeamID(_DefaultZero):
    pass


class GameID(_DefaultBlank):
    pass


class RookieYear(_DefaultBlank):
    pass


class PlayerExperience(_DefaultBlank):
    Rookie = 'Rookie'
    Sophomore = 'Sophomore'
    Veteran = 'Veteran'


class PlayerPosition(_DefaultBlank):
    Forward = 'F'
    Center = 'C'
    Guard = 'G'


class StarterBench(_DefaultBlank):
    Starters = 'Starters'
    Bench = 'Bench'


class DraftYear(_DefaultBlank):
    pass


class DraftPick(_DefaultBlank):
    FirstRound = '1st+Round'
    SecondRound = '2nd+Round'
    FirstPick = '1st+Pick'
    Lottery = 'Lottery+Pick'
    Top5 = 'Top+5+Pick'
    Top10 = 'Top+10+Pick'
    Top15 = 'Top+15+Pick'
    Top20 = 'Top+20+Pick'
    Top25 = 'Top+25+Pick'
    Picks11Thru20 = 'Picks+11+Thru+20'
    Picks21Thru30 = 'Picks+21+Thru+30'
    Undrafted = 'Undrafted'


class College(_DefaultBlank):
    pass


class Country(_DefaultBlank):
    pass


class Height(_DefaultBlank):
    '''
    Example:
    for greater than 6ft8 api call should be GT+6-8
    for lower than 7ft3 api call should be LT+7-3
    '''


class Weight(_DefaultBlank):
    '''
    Example:
    for greater than 225lbs api call should be GT+225lbs
    '''


class Counter:
    Default = '1000'


class Sorter:
    PTS = 'PTS'
    FGM = 'FGM'
    FGA = 'FGA'
    FG_PCT = 'FG_PCT'
    FG3M = 'FG3M'
    FG3A = 'FG3A'
    FG3_PCT = 'FG3_PCT'
    FTM = 'FTM'
    FTA = 'FTA'
    FT_PCT = 'FT_PCT'
    OREB = 'OREB'
    DREB = 'DREB'
    AST = 'AST'
    STL = 'STL'
    BLK = 'BLK'
    TOV = 'TOV'
    REB = 'REB'
    Default = PTS


class Direction:
    DESC = 'DESC'
    ASC = 'ASC'
    Default = DESC