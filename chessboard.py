import pygame

class Chessboard:

    def __init__(self):
        self.image = pygame.image.load('chessboard2.jpg')
        self.chessboard_lattice_width = 30
        self.chessboard_num_of_lattice_per_line = 15
        self.chessboard_color_info = (251, 208, 34, 255)

    def blitme(self,ai):
        """在指定位置绘制棋盘"""
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()

        self.rect = self.image.get_rect()

        self.rect.midtop = self.screen_rect.midtop
        self.screen.blit(self.image, self.rect)
