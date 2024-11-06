from abc import ABC, abstractmethod
class BotStrategy(ABC):
  @abstractmethod
  def next_move(self, board):
    pass