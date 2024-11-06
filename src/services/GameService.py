from src.helpers.GameBuilder import GameBuilder
from src.models.GameStatus import GameStatus
from src.models.PlayerType import PlayerType
from src.models.CellStatus import CellStatus

class GameService:
  def __init__(self):
    self.game = None

  def start_game(self, dimensions, players, winnding_strategies):
    self.game =  GameBuilder().set_dimension(dimensions).set_players(players).set_winning_strategies(winnding_strategies).build()
    return self.game
  
  def display_board(self):
    self.game.board.display_board()
  
  def _ask_cell_input(self):
    while True:
      row = int(input("row -> "))
      col = int(input("col -> "))
      if self.game.board.board[row][col].status != CellStatus.EMPTY:
        print("This is already filled please choose different cell")
        continue
      return row, col
  
  def take_move(self):
    if self.game.next_turn == self.game.board.dimension * self.game.board.dimension:
      self._declare_game_draw()
      return
    player = self.game.players[self.game.next_turn % len(self.game.players)]
    if player.type == PlayerType.PLAYER:
        row, col = self._ask_cell_input()
    else:
      # default bot
      row,col = player.strategy.next_move(self.game.board)
    self.game.board.board[row][col].player = player
    self.game.board.board[row][col].status = CellStatus.FILLED
    self.check_winner1(self.game.board.board[row][col])
    self.game.next_turn = self.game.next_turn + 1
      

  def _declare_winner(self, player):
    self.game.status = GameStatus.FINISHED
    self.game.winner = player
    print("It's a win the winner is " + player.name)
  
  def _declare_game_draw(self):
    self.game.status = GameStatus.DRAW
    print("Game is draw")
  
  def check_winner1(self, cell):
    for winning_strategy in self.game.winning_strategies:
      is_win, player = winning_strategy.check_winner(cell, self.game.board)
      if is_win:
        self._declare_winner(player)