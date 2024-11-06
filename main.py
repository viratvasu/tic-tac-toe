from src.controller.GameController import GameController
from src.services.GameService import GameService
from src.models.Player import Player
from src.models.Bot import Bot
from src.models.PlayerType import PlayerType
from src.models.GameStatus import GameStatus
from src.models.Symbol import Symbol
from src.helpers.strategies.winning_strategies import col, row

gs = GameService()
gc = GameController(gs)
p1 = Player(1, "vasu", PlayerType.PLAYER, Symbol('X'))
p2 = Bot(2, "bot1", PlayerType.BOT, Symbol('y'), "easy")
game = gc.start_game(3, [p1,p2], [col.Col(), row.Row()])

while(game.status == GameStatus.IN_PROGRESS):
  gc.display_board()
  gc.take_move()