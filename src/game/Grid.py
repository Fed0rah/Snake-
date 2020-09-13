from game.Snake import Snake
import pygame

class Grid:
	def __init__(self,screen):
		self.__snake=Snake(screen)
		# self.__food=food()
		self.__length=screen.get_size()[0]
		self.__height=screen.get_size()[1]
		self.screen = screen

		self.__sizeCase = self.__snake.sizeCase
		self.__sizeGrid = self.__snake.sizeGrid

	def draw(self):
		for i in range(self.__sizeGrid):
			for j in range(self.__sizeGrid):
				if i == self.__snake.x and j == self.__snake.y:
					pygame.draw.rect(self.screen, (0, 0, 0), (10+30*i, 10+30*j, 30, 30))

	@property
	def snake(self):
		return self.__snake

