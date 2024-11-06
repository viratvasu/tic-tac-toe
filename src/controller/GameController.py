class GameController:
  def __init__(self, game_service):
    self.gs = game_service
    
  def start_game(self, dimensions, players, winnding_strategies):
    return self.gs.start_game(dimensions, players, winnding_strategies)
  
  def display_board(self):
    self.gs.display_board()
  
  def take_move(self):
    self.gs.take_move()