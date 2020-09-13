
class Snake:
	def __init__(self, screen):
		self.__sizeCase = 30
		self.__sizeGrid = int((screen.get_size()[1]-20)/self.__sizeCase)
		self.__x = int(self.__sizeGrid/2)
		self.__y = int(self.__sizeGrid/2)

	def moveU(self):
		self.__y -= 1

	def moveD(self):
		self.__y += 1

	def moveR(self):
		self.__x += 1

	def moveL(self):
		self.__x -= 1

	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

	@property
	def sizeGrid(self):
		return self.__sizeGrid

	@property
	def sizeCase(self):
		return self.__sizeCase