class GameStats:
	"""Track statistics for alien invasion."""

	def __init__(self , ai_game):
		"""initializet the staticstics"""
		self.settings = ai_game.settings
		self.reset_stats()

		#start the game in inactive mode
		self.game_active = False

		#start alien invasion in an active state
		self.game_active = True

		#high score should never ve reset
		self.high_score = 0

	def reset_stats(self):
		"""initialize the statistics that can change during the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
