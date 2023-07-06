import pygame
import sys
import numpy as np
from chessboard import Chessboard
from check import *
from button import Button
from white_defence import *
from α_β import alpha_beta
from max_min import max_min
from max_10 import max_10

#棋盘通过turtle绘制，共15*15=225个格子，每个格子为30*30（像素）的正方形，棋盘背景色的rgb值为（251，208，34）

class MstFiveGo:

    def __init__(self):
        """初始化游戏并创建资源"""
        pygame.init()

        self.chessboard = Chessboard()

        self.chessboard_lattice_width = self.chessboard.chessboard_lattice_width
        self.chessboard_num_of_lattice_per_line = self.chessboard.chessboard_num_of_lattice_per_line
        self.chessboard_color_info = self.chessboard.chessboard_color_info


        self.screen=pygame.display.set_mode((self.chessboard_lattice_width*self.chessboard_num_of_lattice_per_line,\
                                             self.chessboard_lattice_width*self.chessboard_num_of_lattice_per_line))
                                                                                              # 创建窗口，跟棋盘大小一样

        self.button1 = Button(self, "Man vs Man",(225,172.5))
        self.button2=Button(self,"Man vs Computer",(225,277.5))
        self.black_win_button=Button(self,"Black Wins!",(225,225))
        self.white_win_button = Button(self, "White Wins!", (225, 225))
        self.draw_button=Button(self,"Draw",(225,225))

        pygame.display.set_caption('Mst Five Go')


        self.root=np.zeros((15,15))
        self.validspace=np.zeros((15,15))
        self.black_pos=[]       #分别记录所有黑子和白子的位置信息，作为判断游戏结束的条件
        self.white_pos=[]

        self.flag0=True
        self.flag1=False
        self.flag1_active=True
        self.flag2=False
        self.flag2_active=True


    def run_game(self):
        """运行游戏"""
        i=0                         #i记录鼠标点击次数，根据i的奇偶确定是下黑子还是白子
        self.chessboard.blitme(self)
        self.button1.draw_button()
        self.button2.draw_button()
        pygame.display.flip()
        while self.flag0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button1.rect.collidepoint(mouse_pos):
                        self.flag0=False
                        self.flag1=True
                        self.chessboard.blitme(self)
                    elif self.button2.rect.collidepoint(mouse_pos):
                        self.flag0 = False
                        self.flag2=True
                        self.chessboard.blitme(self)


        while self.flag1:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()

                elif event.type==pygame.MOUSEBUTTONDOWN:         #在鼠标点击处添加棋子
                    if self.flag1_active:
                        mouse_pos = pygame.mouse.get_pos()
                        x = mouse_pos[0]
                        y = mouse_pos[1]
                        root_x=x // self.chessboard_lattice_width
                        root_y=y // self.chessboard_lattice_width
                        new_chess_x = root_x * self.chessboard_lattice_width + \
                                      int(self.chessboard_lattice_width / 2)
                        new_chess_y = root_y * self.chessboard_lattice_width + \
                                      int(self.chessboard_lattice_width / 2)
                        color_info = tuple(pygame.Surface.get_at(self.screen, (new_chess_x, new_chess_y)))


                        if color_info != self.chessboard_color_info:      #若点击处的颜色与棋盘颜色不同，则说明已经有棋子，则不做操作
                            pass

                        elif i % 2 == 0:
                            pygame.draw.circle(self.screen, 'black', (new_chess_x, new_chess_y),\
                                               self.chessboard_lattice_width/3)
                            i += 1
                            self.root[root_y][root_x]=1
                            self.black_pos.append((new_chess_x, new_chess_y))

                            if check(self.black_pos,self):
                                self.flag1_active=False
                                self.black_win_button.draw_button()
                                pygame.display.flip()
                            elif i == 225:
                                self.flag1_active = False
                                self.draw_button.draw_button()
                                pygame.display.flip()

                        else:
                            pygame.draw.circle(self.screen, 'white', (new_chess_x, new_chess_y),\
                                               self.chessboard_lattice_width/3)
                            i += 1
                            self.root[root_y][root_x] = 2
                            self.white_pos.append((new_chess_x, new_chess_y))

                            if check(self.white_pos,self):
                                self.flag1_active=False
                                self.white_win_button.draw_button()
                                pygame.display.flip()
                            elif i == 225:
                                self.flag1_active = False
                                self.draw_button.draw_button()
                                pygame.display.flip()


        while self.flag2:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:  # 在鼠标点击处添加棋子
                    if self.flag2_active:
                        mouse_pos = pygame.mouse.get_pos()
                        x = mouse_pos[0]
                        y = mouse_pos[1]
                        root_x = x // self.chessboard_lattice_width
                        root_y = y // self.chessboard_lattice_width
                        new_chess_x = root_x * self.chessboard_lattice_width + \
                                      int(self.chessboard_lattice_width / 2)
                        new_chess_y = root_y * self.chessboard_lattice_width + \
                                      int(self.chessboard_lattice_width / 2)
                        color_info = tuple(pygame.Surface.get_at(self.screen, (new_chess_x, new_chess_y)))
                        if color_info != self.chessboard_color_info:  # 若点击处的颜色与棋盘颜色不同，则说明已经有棋子，则不做操作
                            pass

                        else :
                            pygame.draw.circle(self.screen, 'black', (new_chess_x, new_chess_y),\
                                               self.chessboard_lattice_width / 3)
                            i += 1
                            self.root[root_y][root_x] = 1
                            self.validspace[max(0,root_y-2):min(15,root_y+3),max(0,root_x-2):min(15,root_x+3)]+=1
                            self.validspace[root_y][root_x]-=25
                            self.black_pos.append((new_chess_x, new_chess_y))
                            pygame.display.flip()
                            if check(self.black_pos, self):
                                self.flag2_active = False
                                self.black_win_button.draw_button()
                                pygame.display.flip()
                            elif i == 225:
                                self.flag2_active = False
                                self.draw_button.draw_button()
                                pygame.display.flip()
                            else:
                                if i<6:
                                    best_choice=max_10(self)
                                else:
                                    best_choice=max_min(self,2,2,-float('inf'),float('inf'))
                                    # best_choice=(-1,-1)
                                    # max_point=-float('inf')
                                    # for i in range(15):
                                    #     for j in range(15):
                                    #         if self.validspace[i][j]>0 and self.root[i][j]==0:
                                    #             self.root[i][j] = 2
                                    #             self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] += 1
                                    #             self.validspace[i][j] -= 25
                                    #             point = alpha_beta(self, 3,l)
                                    #             self.validspace[i][j] += 25
                                    #             self.validspace[max(i - 2, 0):min(j + 3, 15), max(i - 2, 0):min(j + 3, 15)] -= 1
                                    #             self.root[i][j] = 0
                                    #             l.append(point)
                                    #             if point>max_point:
                                    #                 max_point=point
                                    #                 best_choice=(i,j)
                                    # print(len(l))
                                    # print(best_choice)

                                root_y=best_choice[0]
                                root_x=best_choice[1]
                                new_chess_x = root_x * self.chessboard_lattice_width + \
                                              int(self.chessboard_lattice_width / 2)
                                new_chess_y = root_y * self.chessboard_lattice_width + \
                                              int(self.chessboard_lattice_width / 2)
                                pygame.draw.circle(self.screen, 'white', (new_chess_x, new_chess_y),\
                                                   self.chessboard_lattice_width / 3)
                                i += 1
                                self.root[root_y][root_x] = 2
                                self.validspace[max(0, root_y - 2):min(15, root_y + 3),max(0, root_x - 2):min(15, root_x + 3)] += 1
                                self.validspace[root_y][root_x] -= 25
                                self.white_pos.append((new_chess_x, new_chess_y))
                                if check(self.white_pos,self):
                                    self.flag2_active=False
                                    self.white_win_button.draw_button()
                                    pygame.display.flip()
                                elif i == 225:
                                    self.flag2_active = False
                                    self.draw_button.draw_button()
                                    pygame.display.flip()



ai=MstFiveGo()
ai.run_game()