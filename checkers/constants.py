import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

RED = (255, 0, 0) # <- this is red
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
# YELLOW = (230, 213, 90)


CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
RED_WIN = pygame.transform.scale(pygame.image.load("assets/red_winner.jpg"), (350, 100))
BLACK_WIN = pygame.transform.scale(pygame.image.load("assets/black_winner.jpg"), (350, 100))
START = pygame.transform.scale(pygame.image.load("assets/start.jpg"), (700, 200))