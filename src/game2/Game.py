import pygame, sys
import cv2
from src.game2.Snake import *
import numpy as np
import random

class Grid:
	def __init__(self):
		self.taille_fenetre = 2000
		self.taille_grille = 40
		self.Grid = np.zeros((self.taille_grille,self.taille_grille))
		self.Display = np.zeros((self.taille_fenetre,self.taille_fenetre,3))
		self.taille_cellule = int(self.taille_fenetre/self.taille_grille)
	def Update_Display(self):
		for i in range(self.taille_grille):
			for j in range(self.taille_grille):
				#print( "i = {} , j = {}".format(i,j))
				if self.Grid[i][j] == 1:
					for k1 in range(self.taille_cellule*i,self.taille_cellule*(i+1)):
						for k2 in range(self.taille_cellule*j,self.taille_cellule*(j+1)):
							self.Display[k1][k2] = [0,255,0]

				if self.Grid[i][j] == 0:
					for k1 in range(self.taille_cellule * i, self.taille_cellule * (i + 1)):
						for k2 in range(self.taille_cellule * j, self.taille_cellule*(j + 1)):
							self.Display[k1][k2] = [0,0,0]

				if self.Grid[i][j] == 2:
					for k1 in range(self.taille_cellule * i, self.taille_cellule * (i + 1)):
						for k2 in range(self.taille_cellule * j, self.taille_cellule*(j + 1)):
							self.Display[k1][k2] = [0,0,255]

	#def print_grille(self):
		#cv2.imshow("Snake",self.Display)

	def Initialize_Grid(self):
		self.Grid[20][20] = 1
		print(self.Grid[20][20])
		Snk = Snake([[20,20]],self)
		Snk.appear_fruit(self)
		self.Update_Display()
		return Snk,self

class Game:
	def __init__(self,Grid):
		print("Bienvenue dans mon jeu Snake - Première Version")
		self.Grid = Grid()
	#def update(self,Grid2):
		#self.Grid = Grid2

	def run(self):
		self.Grid.Grid[20][20] = int(1)
		print("VALEUR DU PREMIER CARRE AU MILIEU QUI EST CENSÉ MARCHER NOM DE DIEU = {}".format(self.Grid.Grid[20][20]))
		Snake, self.Grid = self.Grid.Initialize_Grid()
		cv2.imshow("Snake",self.Grid.Display)
		key = cv2.waitKey(0)
		bool = True
		while bool:
			if key == ord("z"):
				Snake.moveUP()
				Snake.Update_Snake(self.Grid)
				self.Grid.Update_Display()
				cv2.imshow("Snake",self.Grid.Display)
			if key == ord("d"):
				Snake.moveRight()
				Snake.Update_Snake(self.Grid)
				self.Grid.Update_Display()
				cv2.imshow("Snake",self.Grid.Display)
			if key == ord("q"):
				Snake.moveLeft()
				Snake.Update_Snake(self.Grid)
				self.Grid.Update_Display()
				cv2.imshow("Snake",self.Grid.Display)
			if key == ord("s"):
				Snake.moveDown()
				Snake.Update_Snake(self.Grid)
				self.Grid.Update_Display()
				cv2.imshow("Snake",self.Grid.Display)
			if key == ord("l"):
				print("Vous êtes une merde, Fin du programme")
				break


