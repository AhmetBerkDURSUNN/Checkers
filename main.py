import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE,WHITE
from checkers.game import Game
from pyminimax import minimax

FPS = 60 #introduced a fixed time into the game
#Create a window 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos): # When I press the mouse, we will select where we pressed
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True #It is getting infinite loop  
    clock = pygame.time.Clock() # Use clock keeps the loop at a set constant speed
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False
        
        for event in pygame.event.get(): #Checks if there is any event on the mouse
            
            if event.type == pygame.QUIT: #for quitin the window
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: #for moving the mouse
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()# update board when change pawn coordinators
    print("You win BOSS !")
    pygame.quit()

main()