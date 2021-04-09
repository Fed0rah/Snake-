import pygame, sys
import cv2
from src.game.Snake import Snake
import numpy as np

class Display:
	def __init__(self):
		self.Display = np.zeros((2000,2000, 3))
		pt_vert = [0, 255, 0]
		for i in range(975, 1025):
			for j in range(975, 1025):
				self.Display[i][j] = pt_vert

	def appear_fruit(self):
		pass


class movement:
	def __init__(self,Display,snake):
		self.Display = Display
		self.snake = snake
	def moveUP(self):
		pass
	def moveDown(self):
		pass
	def moveLeft(self):
		pass
	def moveRight(self):
		pass
	def check_move(self):
		pass

class Game:
	def __init__(self,Display):
		print("Bienvenue dans mon jeu Snake - Première Version")
		self.Display = Display


	def run(self):
		pass

	def lose(self):
		pass



