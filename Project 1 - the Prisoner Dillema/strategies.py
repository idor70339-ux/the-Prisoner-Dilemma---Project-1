
#in this file i created the strategies that can be played in the game


# always_cooperate
# returns cooperate no matter what the history of both players were
def always_cooperate(my_history, opp_history):
    return "C"

# always_defect
#  returns defect no matter what the history of both players were
def always_defect(my_history, opp_history):
    return "D"


# tit for tat
# if there is no history, return "cooperate". else, return the last opponents move
def tit_for_tat(my_history, opp_history):
    if len(opp_history) == 0:
        return "C"
    return opp_history[-1]

