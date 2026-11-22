from game_rules import *
from strategies import *
from play_game import *
from play_tournament import *



#strategies tests

#testing if "always_defect" always outputing "D"

def test_always_D():
    assert always_defect([], []) == "D" 
    assert always_defect(["C"], ["D"]) == "D"
    assert always_defect(["C"], ["C"]) == "D"
    assert always_defect(["D"], ["C"]) == "D"
    assert always_defect(["D"], ["D"]) == "D"

test_always_D()

#testing if "always_coopereate" always outputing "C"

def test_always_C():
    assert always_cooperate([], []) == "C"
    assert always_cooperate(["C"], ["C"]) == "C"
    assert always_cooperate(["C"], ["D"]) == "C"
    assert always_cooperate(["D"], ["C"]) == "C"
    assert always_cooperate(["D"], ["D"]) == "C"

test_always_C()

# testing if "tit_for_tat" return "C" if there is no history 

def test_tit_for_tat_no_history():
    assert tit_for_tat([], []) == "C"

test_tit_for_tat_no_history()

#testing if "tit_for_tat" always return the last opponent move

def test_tit_for_tat_yes_history():
    assert tit_for_tat(["C"], ["C"]) == "C"
    assert tit_for_tat(["C"], ["D"]) == "D"
    assert tit_for_tat(["D"], ["C"]) == "C"
    assert tit_for_tat(["D"], ["D"]) == "D"
    assert tit_for_tat(["D", "D"], ["D", "C"]) == "C"

test_tit_for_tat_yes_history()

#test play_game
#testing by predicting the results of tit_for_tat as player 1

def test_play_game_tit_for_tat_3():
    assert play_game(tit_for_tat, always_cooperate, 3, game) == (9, 9)
    assert play_game(tit_for_tat, always_defect, 3, game) == (2, 7)
    assert play_game(tit_for_tat, tit_for_tat, 3, game) == (9, 9)

test_play_game_tit_for_tat_3()

##testing by predicting the results of always_cooperate as player 1

def test_play_game_always_cooperate_3():
    assert play_game(always_cooperate, always_cooperate, 3, game) == (9, 9)
    assert play_game(always_cooperate, always_defect, 3, game) == (0, 15)
    assert play_game(always_cooperate, tit_for_tat, 3, game) == (9, 9)

test_play_game_always_cooperate_3()

##testing by predicting the results of always_defect as player 1

def test_play_game_always_defect_3():
    assert play_game(always_defect, always_cooperate, 3, game) == (15, 0)
    assert play_game(always_defect, always_defect, 3, game) == (3, 3)
    assert play_game(always_defect, tit_for_tat, 3, game) == (7, 2)

test_play_game_always_defect_3()

#testing what will happens if rounds = 0

def test_rounds_zero():
    assert play_game(always_defect, always_cooperate, 0, game) == (0, 0)

test_rounds_zero()

#tournament testing

def test_tournament():
    results1 = play_tournament([always_cooperate, always_defect, tit_for_tat], 1, 10, game_rules)
    assert results1 == {"always_cooperate": 30, "always_defect": 64, "tit_for_tat": 39}
    results2 = play_tournament([always_cooperate, always_defect, tit_for_tat], 1, 5, game_rules)
    assert results2 == {"always_cooperate" : 15, "always_defect" : 34, "tit_for_tat" : 19}

test_tournament()
