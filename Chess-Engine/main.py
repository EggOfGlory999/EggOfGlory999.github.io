"""
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object.
"""

import pygame as p
from Chess_import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #this is for animations.
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called once within the main
'''
def_load_images():
  pieces = ["wP", "wN", "wB", "wR", "wQ", "wK", "bP", "bN", "bB", "bR", "bQ", "bK"]
  for piece in pieces:
    IMAGES[piece] - p.transform.scale(p.image.load(piece + ".png"), (SQ_SIZE, SQ_SIZE))
  
'''
The main driver for our code. This will handle user input and updating the graphics.
'''
def_main():
  p.init()
  screen = p.display.set_mode((WIDTH, HEIGHT))
  clock = p.time.Clock()
  screen.fill(p.Color("white"))
gs = ChessEngine.GameState()
load_images() #only do this once, before the while loop.
running = True
sqSelected = () #no square is selected, keep track of the last click of the user (tuple: (row, col))
playerClicks = [] #keep track of player clicks (two tuples: [(6, 4), (4, 4)])
while running:
  for e in p.event.get():
    if e.type == p.QUIT:
      running = false
    elif e.type == p.MOUSEBUTTONDOWN:
      location = p.mouse.get_pos() #(x, y) location of mouse.
      col = location[0]//SQ_SIZE
      row = location[1]//SQ_SIZE
      if sqSelected == (row, col): #the user clicked on the same square twice.
        sqSelected = () #deselect 
        playerClicks = [] #clear player clicks
      else:
        sqSelected = (row, col)
        playerClicks.append(sqSelected) #append for both 1st and 2nd clicks.
      if len(playerClicks) == 2: #after 2nd click
        
      
    clock.tick(MAX_FPS)
    p.display.flip

    
    
'''
Responsible for all the graphics within a current game state.
'''

def drawGameState(screen, gs):
  drawBoard(screen)
  drawPieces(screen, gs.board)
  
'''
Draw the squares on the board. The top left square is always light.
'''

  
def drawBoard(screen, board):
  colors = [p.Color("powderblue"), p.Color("blue")]
  for r in range(DIMENSION):
    for c in range(DIMENSION):
      color = colors[((r+c)%2)]
      p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
      piece = [r][c]
      if piece != "--": #not empty square
        screen.blit(IMAGES[pieces], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
        
        

  
'''
Draw the pieces on the board using the current GameState.board.
'''


def drawPieces(board):
  for r in range(DIMENSION):
    for c in range(DIMENSION):
      piece = [r][c]
      if piece != "--": #not empty square
        screen.blit(IMAGES[pieces], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
  
  
  
  
  
 if __name__ == "__main__":
  main()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  main()
