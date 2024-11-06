from src.models.Board import Board
from src.models.GameStatus import GameStatus

class GameBoard:
  def __init__(self, dimensions, players, winning_strategies):
    self.board = Board(dimensions)
    self.players = players
    self.winning_strategies = winning_strategies
    self.status = GameStatus.IN_PROGRESS
    self.winner = None
    self.moves = []
    self.next_turn = 0