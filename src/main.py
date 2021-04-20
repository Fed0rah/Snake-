import numpy as np
import cv2

Display = np.zeros((500,500,3),dtype = 'uint8')


class Snake:
	def __init__(self,list_pos,eaten):
		self.list_pos = np.array(list_pos)
		self.head = list_pos[0]
		self.eaten = eaten
		self.apple_position = np.random.randint(0,50,2)*10
	def collisition_display(self):
		return (np.array(self.head) < 0).any() or (np.array(self.head) >= 500).any()

	def collision_with_self(self):
		return (np.linalg.norm(self.head - self.list_pos[2:],axis = 1) ==0).any()


	def collision_with_fruit(self,Display):
		print("Longueur du snake 1 : {}".format(len(self.list_pos)))
		if (self.apple_position == self.head).all():
			a = self.list_pos.tolist()
			a.insert(0,[self.apple_position[0],self.apple_position[1]])
			self.list_pos = np.array(a)

			print("Longueur du snake 2 : {}".format(len(self.list_pos)))
			Display.draw_green(self.list_pos,self.apple_position)
			return True
		else:
			return False
	###Uniquement pour l'aspect joueur il n'y aura pas besoin pour l'implémentation en Q-learning puisque c'est l'ordi qui gère les actions.
	def move(self,k,prev_k,action_prev):

		if k == ord("z") and prev_k != ord("s"):
			return 0
		if k == ord("d") and prev_k != ord("q") :
			return 2
		if k == ord("s") and prev_k != ord("z"):
			return 1
		if k == ord("q") and prev_k != ord("d"):
			return 3
		return action_prev

	## action = 0 : monter
	## action = 1 : descendre
	## action = 2 : droite
	## action = 3 : gauche
	## action = -1 : l'action précedente
	def take_action(self,action,action_prev):
		if action == -1:
			action = action_prev
		if action_prev == 0:
			if action == 0:
				self.list_pos[0][0] -= 10
				self.head = self.list_pos[0]
				self.list_pos[1:] = self.list_pos[:len(self.list_pos) - 1]
			if action == 2:
				self.list_pos[0][1] += 10
				self.head = self.list_pos[0]
				self.list_pos[1:] = self.list_pos[:len(self.list_pos) - 1]
			if action == 3:
				self.list_pos[0][1] -= 10
				self.head = self.list_pos[0]
				self.list_pos[1:] = self.list_pos[:len(self.list_pos) - 1]
		if action_prev == 1:
			if action == 2:
				self.list_pos[0][1] += 10
				self.head = self.list_pos[0]
				self.list_pos[1:] = self.list_pos[:len(self.list_pos) - 1]
			if action == 3:
				self.list_pos[0][1] -= 10
				self.head = self.list_pos[0]
				self.list_pos[1:] = self.list_pos[:len(self.list_pos) - 1]
			if action == 1:
				self.list_pos[0][0] += 10
				self.head = self.list_pos[0]
				self.list_pos[1:] = self.list_pos[:len(self.list_pos) - 1]
		if action_prev == 2:
			if action == 0:
				self.list_pos[0][0] -= 10
				self.head = self.list_pos[0]
				self.list_pos[1:] = self.list_pos[:len(self.list_pos) - 1]
			if action == 2:
				self.list_pos[0][1] += 10
				self.head = self.list_pos[0]
				self.list_pos[1:] = self.list_pos[:len(self.list_pos) - 1]
			if action == 1:
				self.list_pos[0][0] += 10
				self.head = self.list_pos[0]
				self.list_pos[1:] = self.list_pos[:len(self.list_pos) - 1]
		if action_prev == 3:
			if action == 0:
				self.list_pos[0][0] -= 10
				self.head = self.list_pos[0]
				self.list_pos[1:] = self.list_pos[:len(self.list_pos) - 1]

			if action ==1:
				self.list_pos[0][0] += 10
				self.head = self.list_pos[0]
				self.list_pos[1:] = self.list_pos[:len(self.list_pos) - 1]
			if action == 3:
				self.list_pos[0][1] -= 10
				self.head = self.list_pos[0]
				self.list_pos[1:] = self.list_pos[:len(self.list_pos) - 1]
		return self


	def generer_fruit(self):
		self.apple_position = np.random.randint(0,50,2)*10


class Display:
	def __init__(self):
		self.Display = np.zeros((500,500,3))

	def draw_red(self,apple_position):
		self.Display[apple_position[0]:apple_position[0] + 10, apple_position[1]:apple_position[1] +10] = [0,0,255]
	def draw_green(self,list_pos,apple_position = np.array([0,0])):
		if (apple_position == np.array([0,0])).all():

			self.Display = np.zeros((500,500,3))
			for pos in list_pos:
				self.Display[pos[0] : pos[0] + 10,pos[1]: pos[1] + 10] = [0,255,0]
		else:
			self.Display = np.zeros((500, 500, 3))
			self.draw_red(apple_position)
			for pos in list_pos:
				self.Display[pos[0]: pos[0] + 10, pos[1]: pos[1] + 10] = [0, 255, 0]



class Game:
	def __init__(self):
		self.snake = Snake([[250,230],[250,250]],False)
		self.display = Display()


	def run(self):
		alive = True
		self.display.draw_green(self.snake.list_pos)
		self.display.draw_red(self.snake.apple_position)
		cv2.imshow("Snake",self.display.Display)
		action_prev = 2
		prev_k = ord("d")
		while alive:
			key = cv2.waitKey(int(1000/12))
			action = self.snake.move(key,prev_k,action_prev)
			self.snake.take_action(action,action_prev)
			if key != -1 and key != prev_k:
				action_prev = action
				prev_k = key
			self.display.draw_green(self.snake.list_pos,self.snake.apple_position)
			if self.snake.collision_with_fruit(self.display):
				print("il y a eu une collision")
				self.snake.eaten = True
				self.snake.generer_fruit()
			if self.snake.collision_with_self() and not self.snake.eaten:
				alive = False
				print("Vous avez perdu")
			self.snake.eaten = False
			cv2.imshow("Snake",self.display.Display)
			if self.snake.collisition_display():
				alive = False
			if key == 13:
				alive = False







if __name__ == "__main__":
	game = Game()
	game.run()






##take_action : Prends une action dans l'environnement,
#Action : haut, droite ,bas, gauche
#État : List de pos du snk * Position du fruit
#Si jeux, class game qui va hériter de snake. Et c'est là que l'on implémente la vitesse
#Snake.take_action : renvoie un État : (list double par exemple,

#Mon environnement : Correspond au Snake.
#Un État : Correspond à une liste de position du Snake
# take_action : change l'environnement


###CHOSE À FAIRE : - Traiter la collision avec les fruits
##				    - Allongement du Snake avec la collision d'un fruit
#                   - Traiter la collision avec soi même
#                   - Demander Rapidement à Moustapha est-ce que la distinction est claire entre move/take action du point de vu de l'implémentation futur du Q-learning.