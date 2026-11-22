
#the game rules based on the project requirements:

# if both players choose C (cooperate) - both recieve 3 
# if both choose D (defect) - both recieve 1
# if player 1 choose C and player 2 choose D - player 1 recieve 0, player 2 recieve 5
# if player 1 choose D and player 2 choose C - player 1 recieve 5, player 2 recieve 0

game_rules = {("C","C"):(3,3), ("C","D"):(0,5), ("D","D"):(1,1), ("D","C"):(5,0)}

game = game_rules
