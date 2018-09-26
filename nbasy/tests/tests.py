import unittest
from collections import OrderedDict
from nbasy.player_list import PlayerList


class PlayerListTests(unittest.TestCase):
    """
    Tests for the player list class
    """

    def setUp(self):
        self.teams = ['HOU', 'LAL']
        self.players = ['JAMES HARDEN', 'chris PAUL', 'lOnZo BaLl', ]
        self.player_list = PlayerList(
            season='2017-18',
            teams=self.teams,
            players=self.players,
        ).get_player_list()

    def test_get_player_list_basic(self):
        """
        Test the get player list request, default params
        """
        self.assertEqual(type(self.player_list), OrderedDict)

    def test_get_player_list_teams(self):
        """
        Test team filters working correctly, checks every player is from one of listed teams
        """
        for k, v in self.player_list.items():
            self.assertTrue(v["TEAM_ABBREVIATION"] in self.teams)

    def test_get_player_list_players(self):
        """
        Test player filters working correctly, checks every player is in list of players
        """
        self.players = [x.lower() for x in self.players]
        for k, v in self.player_list.items():
            self.assertTrue(k.lower() in self.players)


if __name__ == '__main__':
    unittest.main()
