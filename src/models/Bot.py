from src.models.Player import Player
from src.helpers.strategies.bot_strategies.EasyBotStrategy import EasyBotStrategy

class Bot(Player):
  def __init__(self, id, name, type, symbol, difficulty_level):
    super().__init__(id, name, type, symbol)
    # you can use factory design pattern for this
    if difficulty_level == "easy":
      self.strategy = EasyBotStrategy()
      
  