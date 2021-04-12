class Corps_Snake:
	def __init__(self,front,x,y):
		self.front = front
		self.x = x
		self.y = y
	def move(self):
		self.x = self.front.x
		self.y = self.front.y
class Head:
	def __init__(self,direction,x,y):
		self.direction = direction
		self.x = x
		self.y = y
	def move(self):
		if self.direction == 0:
			self.x += 1
		elif self.direction == 1:
			self.y += 1
		elif self.direction == 2:
			self.x -= 1
		elif self.direction == 3:
			self.y -= 1
