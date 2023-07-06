import numpy as np
from white_defence import boardevaluate_for_white
from black_defence import boardevaluate_for_black
#未考虑棋盘下满的情况
#递归调用函数

# def alpha_beta(self,leftstep,n,passvalue):
#
#     alpha=passvalue
#
#     if n%2==0:#考虑的最后一步为玩家走，偏向防守
#         if leftstep==1:
#             for i in range(15):
#                 for j in range(15):
#                     if self.validspace[i][j]>0 and self.root[i][j]==0:
#                         self.root[i][j] = 1
#                         point=boardevaluate_for_white(self.root,'black')-boardevaluate_for_white(self.root,'white')
#                         self.root[i][j] = 0
#                         if point>alpha:
#                             alpha=point
#             return -alpha
#
#         elif leftstep%2==0:#AI
#             for i in range(15):
#                 for j in range(15):
#                     if self.validspace[i][j]>0 and self.root[i][j]==0:
#                         self.root[i][j] = 2
#                         self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] += 1
#                         self.validspace[i][j] -= 25
#                         point = -alpha_beta(self, leftstep - 1,n,alpha)
#                         self.validspace[i][j] += 25
#                         self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] -= 1
#                         self.root[i][j] = 0
#                         if point>alpha:
#                             alpha=point
#             return -alpha
#
#         else:#玩家
#             for i in range(15):
#                 for j in range(15):
#                     if self.validspace[i][j]>0 and self.root[i][j]==0:
#                         self.root[i][j] = 1
#                         self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] += 1
#                         self.validspace[i][j] -= 25
#                         point = -alpha_beta(self, leftstep - 1,n,alpha)
#                         self.validspace[i][j] += 25
#                         self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] -= 1
#                         self.root[i][j] = 0
#                         if point>alpha:
#                             alpha=point
#             return -alpha
#
#     else:#考虑的最后一步为AI走，偏向进攻
#         if leftstep == 1:
#             for i in range(15):
#                 for j in range(15):
#                     if self.validspace[i][j] > 0 and self.root[i][j] == 0:
#                         self.root[i][j] = 2
#                         point = boardevaluate_for_white(self.root, 'white') - boardevaluate_for_white(self.root,'black')
#                         self.root[i][j] = 0
#             return 0
#
#         elif leftstep % 2 == 0:  # 玩家
#             for i in range(15):
#                 for j in range(15):
#                     if self.validspace[i][j] > 0 and self.root[i][j] == 0:
#                         self.root[i][j] = 1
#                         self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] += 1
#                         self.validspace[i][j] -= 25
#                         point = -alpha_beta(self, leftstep - 1, n, alpha)
#                         self.validspace[i][j] += 25
#                         self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] -= 1
#                         self.root[i][j] = 0
#
#         else:  # AI
#             for i in range(15):
#                 for j in range(15):
#                     if self.validspace[i][j] > 0 and self.root[i][j] == 0:
#                         self.root[i][j] = 2
#                         self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] += 1
#                         self.validspace[i][j] -= 25
#                         point = -alpha_beta(self, leftstep - 1, n, alpha)
#                         self.validspace[i][j] += 25
#                         self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] -= 1
#                         self.root[i][j] = 0


















# def alpha_beta(self):
#     best_choice = (-1,-1)
#     max_min_point=-100000000
#     for i in range(15):
#         for j in range(15):
#             if self.validspace[i][j]>0 and self.root[i][j]==0:
#                 self.root[i][j]=2
#                 self.validspace[max(i-2,0):min(i+3,15),max(j-2,0):min(j+3,15)]+=1
#                 self.validspace[i][j]-=25
#                 min_max_point=100000000
#                 for i1 in range(15):
#                     for j1 in range(15):
#                         if self.validspace[i1][j1]>0 and self.root[i1][j1]==0:
#                             self.root[i1][j1] = 1
#                             self.validspace[max(i1 - 2, 0):min(i1 + 3, 15), max(j1 - 2, 0):min(j1 + 3, 15)] += 1
#                             self.validspace[i1][j1] -= 25
#                             max_point=-100000000
#                             cut2=False
#                             for i2 in range(15):
#                                 for j2 in range(15):
#                                     if self.validspace[i2][j2] > 0 and self.root[i2][j2]== 0:#如果有存在大于min_max_point的分数，则cut
#                                         self.root[i2][j2] = 2
#                                         point=boardevaluate_for_white(self.root,'white')-boardevaluate_for_white(self.root,'black')
#                                         if point>min_max_point:
#                                             cut2=True
#                                             self.root[i2][j2] = 0
#                                             break
#                                         elif point>max_point:
#                                             max_point=point
#                                         self.root[i2][j2] = 0
#                                 if cut2:
#                                     break
#                             if not cut2:
#                                 min_max_point=max_point#找最小的那个分数
#                             self.validspace[i1][j1] += 25
#                             self.validspace[max(i1 - 2, 0):min(i1 + 3, 15), max(j1 - 2, 0):min(j1 + 3, 15)] -= 1
#                             self.root[i1][j1] = 0
#                         else:
#                             pass
#                 if min_max_point>max_min_point:
#                     max_min_point=min_max_point
#                     best_choice=(i,j)
#                 self.validspace[i][j] += 25
#                 self.validspace[max(i - 2, 0):min(i + 3, 15), max(j - 2, 0):min(j + 3, 15)] -= 1
#                 self.root[i][j] = 0
#             else:
#                 pass
#     return best_choice
#

def alpha_beta(self,leftstep,l):

    if leftstep==1:
        min_point = float('inf')
        for i in range(15):
            for j in range(15):
                if self.validspace[i][j] > 0 and self.root[i][j] == 0:
                    self.root[i][j] = 1
                    point = boardevaluate_for_white(self.root,'white')-boardevaluate_for_white(self.root,'black')
                    l.append(point)
                    self.root[i][j] = 0
                    if point < min_point:
                        min_point = point
        return min_point

    elif leftstep%2==0:
        max_point=-float('inf')
        for i in range(15):
            for j in range(15):
                if self.validspace[i][j] > 0 and self.root[i][j] == 0:
                    self.root[i][j] = 2
                    self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] += 1
                    self.validspace[i][j] -= 25
                    point = alpha_beta(self, leftstep - 1,l)
                    l.append(point)
                    self.validspace[i][j] += 25
                    self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] -= 1
                    self.root[i][j] = 0
                    if point>max_point:
                        max_point=point
        return max_point

    else:
        min_point = float('inf')
        for i in range(15):
            for j in range(15):
                if self.validspace[i][j] > 0 and self.root[i][j] == 0:
                    self.root[i][j] = 1
                    self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] += 1
                    self.validspace[i][j] -= 25
                    point = alpha_beta(self, leftstep - 1,l)
                    l.append(point)
                    self.validspace[i][j] += 25
                    self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] -= 1
                    self.root[i][j] = 0
                    if point < min_point:
                        min_point = point
        return min_point