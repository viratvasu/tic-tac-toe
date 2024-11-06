from src.models.CellStatus import CellStatus

class Cell:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.status = CellStatus.EMPTY
    self.player = None
  
  def display_cell(self):
    if self.status == CellStatus.EMPTY:
      print("| - |", end="")
    else:
      print(f"| {self.player.symbol.symbol} | ", end="")
  
  def __str__(self):
    return self.__class__.__name__