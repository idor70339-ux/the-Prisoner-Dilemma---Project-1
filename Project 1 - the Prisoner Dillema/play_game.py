

from game_rules import *
from strategies import *



def play_game(strategy1, strategy2, rounds, game):

    #before starting 1st round, the history of each player is blank. after each round, the last move added to the history list
    player_1_history = []
    player_2_history = []

    #before starting 1st round, the score of each player is 0. after each round, the score added to the total score
    tot_1_score = 0 
    tot_2_score = 0 
    for round_number in range(rounds):

        #player 1 choose his move
        move_player_1 = strategy1(player_1_history, player_2_history)

        #player 2 choose his move
        move_player_2 = strategy2(player_2_history, player_1_history)

        #player 1 score
        score_1 = game[move_player_1, move_player_2][0]

        #player 2 score
        score_2 = game[move_player_1, move_player_2][1]

        #addidng the current score to the tottal score
        tot_1_score += score_1
        tot_2_score += score_2

        #addidng the last move of each player to the history of each player
        player_1_history.append(move_player_1)
        player_2_history.append(move_player_2)
    #return the tottal score after the whole game
    return tot_1_score, tot_2_score

play_game(tit_for_tat, always_defect, 3, game) 
#first game: results = (2, 7)
play_game(always_defect, always_cooperate, 3, game) 
#second game: results = (15, 0) 
play_game(always_defect, always_defect, 3, game)
#third game: results = (3, 3)



