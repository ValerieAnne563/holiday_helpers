"""
opponent: A for Rock, B for Paper, and C for Scissors. 
you: X for Rock, Y for Paper, and Z for Scissors.

(1 for Rock, 2 for Paper, and 3 for Scissors)
(0 if you lost, 3 if the round was a draw, and 6 if you won).


A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

Part 2

"Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
"""

OPPONENT_ROCK = 'A'
OPPONENT_PAPER = 'B'
OPPONENT_SCISSORS = 'C'

YOUR_ROCK = 'X'
YOUR_PAPER = 'Y'
YOUR_SCISSORS = 'Z'

choice_score = {
	YOUR_ROCK: 1, # Rock
	YOUR_PAPER: 2, # Paper
	YOUR_SCISSORS: 3  # Scissors
}

same = {
	OPPONENT_ROCK: YOUR_ROCK,
	OPPONENT_PAPER: YOUR_PAPER,
	OPPONENT_SCISSORS: YOUR_SCISSORS
}

# value defeats key
wins = {
	OPPONENT_SCISSORS: YOUR_ROCK,
	OPPONENT_ROCK: YOUR_PAPER,
	OPPONENT_PAPER: YOUR_SCISSORS
}


# key defeats value
losses = {
	OPPONENT_SCISSORS: YOUR_PAPER,
	OPPONENT_ROCK: YOUR_SCISSORS,
	OPPONENT_PAPER: YOUR_ROCK
}


inputs = [
['A', 'Y'],
['B', 'X'],
['C', 'Z']]

score = 0

OUTCOME_LOSS = 'X'
OUTCOME_DRAW = 'Y'
OUTCOME_WIN = 'Z'

with open('input_02.txt') as f:
	# for opponent, you in inputs:
	for line in f.readlines():
		opponent, outcome = line.strip().split(' ')

		if outcome == OUTCOME_DRAW:
			print('Draw')
			score += 3  # Draw
			weapon = same[opponent]
		elif outcome == OUTCOME_WIN:
			print('Win')
			score += 6 # Win!
			weapon = wins[opponent]
		else:
			print('Lost')
			score += 0 # Lost.
			weapon = losses[opponent]

		score += choice_score[weapon]

	print("Your score: %d " % score)

