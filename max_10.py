import numpy as np
from white_defence import boardevaluate_for_white

def max_10(self):
    max_point=-100000000
    best_choice=(-1,-1)
    for i in range(15):
        for j in range(15):
            if self.validspace[i][j] > 0 and self.root[i][j] == 0:
                self.root[i][j] = 2
                point = boardevaluate_for_white(self.root, 'white') - boardevaluate_for_white(self.root, 'black')
                self.root[i][j] = 0
                if point>max_point:
                    max_point = point
                    best_choice=(i,j)
    return best_choice