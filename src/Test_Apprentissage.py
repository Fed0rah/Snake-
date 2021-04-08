import cv2
import numpy as np
import keyboard

def creer_image(longueur,largeur):
	display = np.zeros((longueur,largeur,3))
	return display

def bouger_image(longueur,largeur,pos):
	display = creer_image(longueur,largeur)
	display[pos[0],pos[1]] = [0,0,255]

	cv2.imshow("Test",display)
	key = cv2.waitKey(0)
	return key,display

pos = [100,100]
while True:
	key =  bouger_image(200,200,pos)[0]
	display = bouger_image(200,200,pos)[1]


	if key == 0:
		cv2.imshow("Test", display)
		key = cv2.waitKey(0)
		display[pos[0],pos[1]] = [0, 0, 0]
		display[pos[0] - 10,pos[1]] = [0, 0, 255]
		pos = [pos[0] - 10,pos[1]]
		cv2.imshow("Test",display)
		key = cv2.waitKey(0)
		print(key)
	if key == 1:
		cv2.imshow("Test", display)
		key = cv2.waitKey(0)
		display[pos[0], pos[1]] = [0, 0, 0]
		display[pos[0] + 10, pos[1]] = [0, 0, 255]
		pos = [pos[0] + 10,pos[1]]
		cv2.imshow("Test", display)
		key = cv2.imshow("Test",display)
		print(key)
	if key == 13:
		print(key)
		break








