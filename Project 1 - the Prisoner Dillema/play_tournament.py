from strategies import always_cooperate, always_defect, tit_for_tat
from game_rules import game_rules

#creating a turnament  function that receives inputs of the strategies, the number of games each match would be,  the number of rounds in each game and the game rules. 
#then the function will return an output of a summary of the games results of each strategy
#every player plays two different game. no delf play
def play_tournament(strategies, games_per_pair, rounds_per_game, game):
    score = {}
    #every strategy start at 0

    for strategy in strategies:
        score[strategy.__name__] = 0
#go over every possible couple by creating a matrix of all the strategies and pick strategy i with strategy i+1

    for i in range(len(strategies)):
        for j in range(i + 1, len(strategies)):
            player_1 = strategies[i]
            player_2 = strategies[j]

            # play the pair games_per_pair times
            for _ in range(games_per_pair):
                score_1, score_2 = play_game(player_1, player_2, rounds_per_game, game)
                # add this game's points to each player's total
                score[player_1.__name__] += score_1
                score[player_2.__name__] += score_2

    return score


#always_defect strategy won the tournament with 64 points
play_tournament([always_cooperate, always_defect, tit_for_tat], 1, 10, game_rules)

#always_defect strategy won the tournament with 34 points
play_tournament([always_cooperate, always_defect, tit_for_tat], 1, 5, game_rules)
