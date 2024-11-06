from src.models.Cell import Cell

class Board:
  def __init__(self, dimension):
    self.dimension = dimension
    self.board = [[Cell(i, j) for j in range(dimension)] for i in range(dimension)]
  
  def display_board(self):
    for row in self.board:
      for col in row:
        col.display_cell()
      print("")
  
  def __str__(self):
    return self.__class__.__name__