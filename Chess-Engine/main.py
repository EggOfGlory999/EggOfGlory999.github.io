"""
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object.
"""

import pygame as p
from Chess_import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called once within the main
'''
def_load_images():
  IMAGES["wP"] - p.image.load("3409_white-pawn.png")
  IMAGES["bP"] - p.image.load("3403_black-pawn.png")
  IMAGES["wN"] - p.image.load("3408_white-knight.png")
  IMAGES["bN"] - p.image.load("3402_black-knight.png")
  IMAGES["wB"] - p.image.load("3407_white-bishop.png")
  IMAGES["bB"] - p.image.load("3401_black-bishop.png")
  IMAGES["wR"] - p.image.load("3406_white-rook.png")
  IMAGES["bR"] - p.image.load("3400_black-rook.png")
  IMAGES["wQ"] - p.image.load("3405_white-queen.png")
  IMAGES["bQ"] - p.image.load("3399_black-queen.png")
  IMAGES["wK"] - p.image.load("3404_white-king.png")
  IMAGES["bK"] - p.image.load("3398_black-king.png")
  
  '''
  The main driver for our code. This will handle user input and updating the graphics.
  '''
