
import threading
import time
import boards
import graphics
import kakuro
from kakuro import Kakuro

board = boards.expert2

if __name__ == '__main__':
    kak = Kakuro(board, filtering=3, variable_ordering=None, value_ordering=None)

    def solve():
        start = time.time()
        result = kakuro.backtrack(kak)
        end = time.time()
        print(result)
        print("Time: %.1f" % (end - start))

    thr = threading.Thread(target=solve)
    thr.start()
    graphics.start_graphic(kak)

