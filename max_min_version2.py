import numpy as np
from white_defence import boardevaluate_for_white
from black_defence import boardevaluate_for_black

def valid(self):
    avaliable=[]
    for i in range(15):
        for j in range(15):
            if self.validspace[i][j]>0 and self.root[i][j]==0:
                avaliable.append((i,j))
    return avaliable



def max_min(self,leftstep,n,alpha,beta):#leftstep一定为奇数，即考虑的最后一步一定为AI下
    """计算某个点位的得分"""


    avaliable=valid(self)
    max_point = alpha
    min_point = beta

    if leftstep==1:
        for place in avaliable:
            self.root[place[0]][place[1]] = 2
            point=boardevaluate_for_white(self.root,'white')-boardevaluate_for_white(self.root,'black')
            self.root[place[0]][place[1]] = 0
            if point >= min_point:
                return 100000000
            if point > max_point:
                max_point = point
        return max_point

    elif leftstep==n:
        best_choice=(-1,-1)
        for place in avaliable:
            self.root[place[0]][place[1]] = 2
            self.validspace[max(place[0] - 2, 0):min(place[0] + 3, 15), max(place[1] - 2, 0):min(place[1] + 3, 15)] += 1
            self.validspace[place[0]][place[1]] -= 25
            point = max_min(self, leftstep - 1, n,max_point,min_point)
            self.validspace[place[0]][place[1]] += 25
            self.validspace[max(place[0] - 2, 0):min(place[0] + 3, 15), max(place[1] - 2, 0):min(place[1] + 3, 15)] -= 1
            self.root[place[0]][place[1]] = 0
            if point>max_point:
                max_point = point
                best_choice=(place[0],place[1])
        return best_choice

    elif leftstep%2==1:
        for place in avaliable:
            self.root[place[0]][place[1]] = 2
            self.validspace[max(place[0] - 2, 0):min(place[0] + 3, 15), max(place[1] - 2, 0):min(place[1] + 3, 15)] += 1
            self.validspace[place[0]][place[1]] -= 25
            point = max_min(self, leftstep - 1, n, max_point, min_point)
            self.validspace[place[0]][place[1]] += 25
            self.validspace[max(place[0] - 2, 0):min(place[0] + 3, 15), max(place[1] - 2, 0):min(place[1] + 3, 15)] -= 1
            self.root[place[0]][place[1]] = 0
            if point>=min_point:
                return 100000000
            if point>max_point:
                max_point=point
        return max_point

    else:
        for place in avaliable:
            self.root[place[0]][place[1]] = 1
            self.validspace[max(place[0] - 2, 0):min(place[0] + 3, 15), max(place[1] - 2, 0):min(place[1] + 3, 15)] += 1
            self.validspace[place[0]][place[1]] -= 25
            point = max_min(self, leftstep - 1, n, max_point, min_point)
            self.validspace[place[0]][place[1]] += 25
            self.validspace[max(place[0] - 2, 0):min(place[0] + 3, 15), max(place[1] - 2, 0):min(place[1] + 3, 15)] -= 1
            self.root[place[0]][place[1]] = 0
            if point<=max_point:
                return -100000000
            if point<min_point:
                min_point=point
        return min_point