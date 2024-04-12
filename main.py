import sys

import pygame

pygame.init()
window = pygame.display.set_mode((250, 250))
pygame.display.set_caption("Tic Tac Toe")

background = pygame.image.load("static/board-2097446_640.jpg")
circle = pygame.image.load("static/circle.jpg")
cross = pygame.image.load("static/cross.jpg")

background = pygame.transform.scale(background, (250, 250))
circle = pygame.transform.scale(circle, (50, 50))
cross = pygame.transform.scale(cross, (50, 50))

coor = [[(45, 30), (100,30), 0,0],
        [(0,0), (100,95), 0,0],
        [(0,0), (0,0), 0,0]]

board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

turn = 'X'
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit()
            sys.exit()

    window.blit(background, (0, 0))
    window.blit(circle, (45, 30))
    window.blit(cross, (100, 95))
    pygame.display.update()

    clock.tick(30)
