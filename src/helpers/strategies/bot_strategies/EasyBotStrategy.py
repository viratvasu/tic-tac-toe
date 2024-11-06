from src.helpers.strategies.bot_strategies.strategy import BotStrategy
from src.models.CellStatus import CellStatus

class EasyBotStrategy(BotStrategy):
  def next_move(self, board):
    for i in range(len(board.board)):
      for j in range(len(board.board)):
        if board.board[i][j].status == CellStatus.EMPTY:
          return i, j
    