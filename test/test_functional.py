# players_test.py
import unittest
from football_players import *
from test.TestUtils import TestUtils

class PlayersTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_file_path = "football_players.txt"
        cls.test_utils_instance = TestUtils()

    def test_count_players(self):
        expected_player_count = 15
        actual_player_count = count_players(self.test_file_path)
        self.test_utils_instance.yakshaAssert("TestCountPlayers", expected_player_count == actual_player_count, "functional")
        if expected_player_count == actual_player_count:
            print(f"Number of players counted correctly: {actual_player_count}")
            print("TestCountPlayers = Passed")
        else:
            print(f"Number of players counted incorrectly: {actual_player_count}")
            print("TestCountPlayers = Failed")

    def test_find_youngest_player(self):
        expected_youngest_player = {'Name': 'Kylian Mbappe', 'Age': 23}
        actual_youngest_player = find_youngest_player(self.test_file_path)
        self.test_utils_instance.yakshaAssert("TestFindYoungestPlayer", expected_youngest_player == actual_youngest_player, "functional")
        if expected_youngest_player == actual_youngest_player:
            print(f"Youngest player found correctly: {actual_youngest_player}")
            print("TestFindYoungestPlayer = Passed")
        else:
            print(f"Youngest player found incorrectly: {actual_youngest_player}")
            print("TestFindYoungestPlayer = Failed")

    def test_find_goals_by_messi(self):
        expected_goals = 45
        actual_goals = find_goals_by_messi(self.test_file_path)
        self.test_utils_instance.yakshaAssert("TestFindGoalsByMessi", expected_goals == actual_goals, "functional")
        if expected_goals == actual_goals:
            print(f"Goals scored by Lionel Messi found correctly: {actual_goals}")
            print("TestFindGoalsByMessi = Passed")
        else:
            print(f"Goals scored by Lionel Messi found incorrectly: {actual_goals}")
            print("TestFindGoalsByMessi = Failed")

    def test_find_country_of_ronaldo(self):
        expected_origin = "Funchal"
        actual_origin = find_country_of_ronaldo(self.test_file_path)
        self.test_utils_instance.yakshaAssert("TestFindCountryOfRonaldo", expected_origin == actual_origin, "functional")
        if expected_origin == actual_origin:
            print(f"Cristiano Ronaldo's country found correctly: {actual_origin}")
            print("TestFindCountryOfRonaldo = Passed")
        else:
            print(f"Cristiano Ronaldo's country found incorrectly: {actual_origin}")
            print("TestFindCountryOfRonaldo = Failed")

    def test_count_zero_goal_players(self):
        expected_zero_goal_count = 3
        actual_zero_goal_count = count_zero_goal_players(self.test_file_path)
        self.test_utils_instance.yakshaAssert("TestCountZeroGoalPlayers", expected_zero_goal_count == actual_zero_goal_count, "functional")
        if expected_zero_goal_count == actual_zero_goal_count:
            print(f"Number of zero goal players counted correctly: {actual_zero_goal_count}")
            print("TestCountZeroGoalPlayers = Passed")
        else:
            print(f"Number of zero goal players counted incorrectly: {actual_zero_goal_count}")
            print("TestCountZeroGoalPlayers = Failed")

    def test_find_brand_for_ramos(self):
        expected_brand = "Adidas"
        actual_brand = find_brand_for_ramos(self.test_file_path)
        self.test_utils_instance.yakshaAssert("TestFindBrandForRamos", expected_brand == actual_brand, "functional")
        if expected_brand == actual_brand:
            print(f"Sergio Ramos's sponsor brand found correctly: {actual_brand}")
            print("TestFindBrandForRamos = Passed")
        else:
            print(f"Sergio Ramos's sponsor brand found incorrectly: {actual_brand}")
            print("TestFindBrandForRamos = Failed")

    def test_find_player_type_for_modric(self):
        expected_player_type = "Midfielder"
        actual_player_type = find_player_type_for_modric(self.test_file_path)
        self.test_utils_instance.yakshaAssert("TestFindPlayerTypeForModric", expected_player_type == actual_player_type, "functional")
        if expected_player_type == actual_player_type:
            print(f"Luka Modric's player type found correctly: {actual_player_type}")
            print("TestFindPlayerTypeForModric = Passed")
        else:
            print(f"Luka Modric's player type found incorrectly: {actual_player_type}")
            print("TestFindPlayerTypeForModric = Failed")

    def test_count_experienced_players(self):
        expected_experienced_count = 7
        actual_experienced_count = count_experienced_players(self.test_file_path)
        self.test_utils_instance.yakshaAssert("TestCountExperiencedPlayers", expected_experienced_count == actual_experienced_count, "functional")
        if expected_experienced_count == actual_experienced_count:
            print(f"Number of experienced players counted correctly: {actual_experienced_count}")
            print("TestCountExperiencedPlayers = Passed")
        else:
            print(f"Number of experienced players counted incorrectly: {actual_experienced_count}")
            print("TestCountExperiencedPlayers = Failed")

if __name__ == '__main__':
    unittest.main()
