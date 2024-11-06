from src.CustomExceptions import InvalidPlayerException
from src.models.GameBoard import GameBoard

class GameBuilder:
  def __init__(self):
    self.dimension = None
    self.players = None
    self.winning_strategies = None
  
  def set_dimension(self, dimension):
    self.dimension = dimension
    return self
  
  def set_players(self, players):
    self.players = players
    return self
  
  def set_winning_strategies(self, strategies):
    self.winning_strategies = strategies
    return self
  
  def validate(self):
    if self.dimension - 1 > len(self.players):
      raise InvalidPlayerException() 
    
  def build(self):
    self.validate()
    return GameBoard(self.dimension, self.players, self.winning_strategies)
    