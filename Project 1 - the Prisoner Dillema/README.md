# Iterated Prisoner's Dilemma

## What is this?
A simulation of the Iterated Prisoner's Dilemma. Two players play several rounds; in each round, each player chooses to Cooperate ("C") or Defect ("D"), and earns points according to the game rules. Each player's choice is made by a strategy, which can look at the history of previous moves.

## Files
- `game_rules.py` – the payoff dictionary: each pair of moves maps to the scores of (player 1, player 2).
- `strategies.py` – the strategies. Each takes `(my_history, opp_history)` and returns "C" or "D".
- `play_game.py` – `play_game(strategy1, strategy2, rounds, game)`: plays a full game and returns the total scores of both players.
- `test_play_game.py` – tests for the strategies and for `play_game`.

## How to run
Play a game:
    from play_game import *
    print(play_game(tit_for_tat, always_defect, 3, game_rules))   # (2, 7)

Run the tests:
    pytest

## Strategies
- **always_cooperate** – always plays "C".
- **always_defect** – always plays "D".
- **tit_for_tat** – plays "C" in the first round, then copies the opponent's last move.