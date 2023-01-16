import pygame
#There is a Color get_color() method that returns the color of the pawn.

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8 , 8 #There is an n parameter in the constructor that specifies the side length of the square
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('checkers/crown.png'), (44, 25))