"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
from sample_players import (RandomPlayer, open_move_score,
							improved_score, center_score)
from game_agent import (MinimaxPlayer, AlphaBetaPlayer, custom_score,
						custom_score_2, custom_score_3)

from importlib import reload


class IsolationTest(unittest.TestCase):
	"""Unit tests for isolation agents"""

	def setUp(self):
		self.player2 = RandomPlayer()
		self.player1 = AlphaBetaPlayer(score_fn=custom_score)
		self.game = isolation.Board(self.player1, self.player2)        

	def test(self):
		winner, history, outcome = self.game.play()		
		print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
		print(self.game.to_string())
		print("Move history:\n{!s}".format(history))

if __name__ == '__main__':
	unittest.main()
