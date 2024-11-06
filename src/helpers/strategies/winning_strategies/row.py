from src.helpers.strategies.winning_strategies.strategy import WinningStrategy
from src.models.CellStatus import CellStatus

class Row(WinningStrategy):
  def check_winner(self, cell, board):
    is_won = True
    for i in range(board.dimension):
      if board.board[i][cell.col].status == CellStatus.FILLED and board.board[i][cell.col].player is cell.player:
        continue
      else:
        is_won = False
    return is_won, cell.player