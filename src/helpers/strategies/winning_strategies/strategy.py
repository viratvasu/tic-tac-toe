from abc import ABC, abstractmethod

class WinningStrategy(ABC):

  @abstractmethod
  def check_winner(self, cell, board):
    pass