import random
import numpy as np

class Snake:
	def __init__(self,pos,Grid):
		self.pos = pos #Liste de position représentant le snake, Dans Grid
		self.Grid = Grid
		self.n = len(pos)

	def Evolve_Snake(self,pos_fruit): ##pos_fruit : Création d'une nouvelle tête à cet endroit et d'un nouveau fruit encore une fois dans le Grid
		self.pos.append([pos_fruit])
		self.n += 1
		self.appear_fruit()

	def moveUP(self):
		self.pos[self.n-1] = [self.pos[self.n-1][0] - 1, self.pos[self.n-1][1]]
		for i in range(self.n-1):
			self.pos[i] = self.pos[i+1]
	def moveDown(self):
		self.pos[self.n - 1] = [self.pos[self.n-1][0] + 1, self.pos[self.n-1][1]]
		for i in range(self.n-1):
			self.pos[i] = self.pos[i+1]
	def moveLeft(self):
		self.pos[self.n - 1] = [self.pos[self.n-1][0],self.pos[self.n -1][1] - 1]
		for i in range(self.n-1):
			self.pos[i] = self.pos[i+1]

	def moveRight(self):
		self.pos[self.n - 1] = [self.pos[self.n - 1][0], self.pos[self.n - 1][1] + 1]
		for i in range(self.n-1):
			self.pos[i] = self.pos[i+1]

	def check_move(self,pos_futur,Grid):
		if pos_futur in self.pos:
			return False
		if pos_futur[0] > Grid.taille_cellule or pos_futur[1] > Grid.taille_cellule:
			return False
		return True

	def appear_fruit(self,Grid):
		i, j = random.randint(0,Grid.taille_grille), random.randint(0, Grid.taille_grille)
		while [i,j] in self.pos:
			i, j = random.randint(0,40), random.randint(0,40)
		Grid.Grid[i][j] = 2

	def Update_Snake(self,Grid):
		for i in range(self.n):
			Grid.Grid[self.pos[i][0]][self.pos[i][1]] = 1

