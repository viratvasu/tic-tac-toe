from src.helpers.strategies.winning_strategies.strategy import WinningStrategy
from src.models.CellStatus import CellStatus

class Col(WinningStrategy):

  def check_winner(self, cell, board):
    is_won = True
    for i in range(board.dimension):
      if board.board[cell.row][i].status == CellStatus.FILLED and board.board[cell.row][i].player is cell.player:
        continue
      else:
        is_won = False
    return is_won, cell.player

  def __str__(self):
    return self.__class__.__name__