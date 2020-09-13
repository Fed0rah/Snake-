from game.Grid import Grid
import pygame, sys

class Game:
	def __init__(self):
		pygame.init()
		self.screen=pygame.display.set_mode((1080,720))
		pygame.display.set_caption('Snake AI')
		self.__fps=30
		self.__grid=Grid(self.screen)

	def run(self):
		game_over=False
		clock= pygame.time.Clock()
		while not game_over:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					game_over=True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.__grid.snake.moveU()
					if event.key == pygame.K_LEFT:
						self.__grid.snake.moveL()
					if event.key == pygame.K_RIGHT:
						self.__grid.snake.moveR()
					if event.key == pygame.K_DOWN:
						self.__grid.snake.moveD()

			self.__grid.draw()
			self.screen.fill((0, 0, 0))
			pygame.draw.rect(self.screen, (0, 111, 0), (100, 100, 200, 300))
			pygame.display.update()
			clock.tick(self.__fps)

		pygame.quit()