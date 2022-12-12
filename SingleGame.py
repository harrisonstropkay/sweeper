import numpy as np
import Minefield
from Minefield import *
class SingleGame:
    HIDDEN = -1
    BOMB = -2
    FLAGGED = -3

    def __init__(self, tiles_height, tiles_width, num_bombs) -> None:
        self.tiles_height = tiles_height
        self.tiles_width = tiles_height
        self.minefield = Minefield(tiles_height, tiles_width, num_bombs)
        self.gamefield = np.full((tiles_height, tiles_width), SingleGame.HIDDEN)

    def __str__(self) -> str:
        result = buffer()
        # add x indices
        for x in range(self.tiles_width):
            result += buffer(x)
        result += "\n"
        # add y indices and tile values
        for y in range(self.tiles_height):
            result += buffer(y)
            for x in range(self.tiles_width):
                match self.gamefield[y, x]:
                    case SingleGame.HIDDEN:
                        result += buffer()
                    case SingleGame.BOMB:
                        result += buffer('*')
                        break
                    case SingleGame.FLAGGED:
                        result += buffer('F')
                    case _:
                        result += buffer(str(self.gamefield[y, x]))
            result += "\n"
        return result

    # returns True if game is won, False if lost
    def play(self) -> bool:
        print(self)
        # game loop
        while (True):
            # get player guess
            line = input("Guess: ")
            line_split = line.split()
            y = int(line_split[0])
            x = int(line_split[1])

            result = self.minefield.reveal_tile(y, x)
            self.gamefield[y, x] = result
            print(self)
            if result == -1:
                return False


test_game = SingleGame(10, 10, 12)
print(test_game.minefield)
test_game.play()
