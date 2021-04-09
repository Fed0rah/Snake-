import cv2
import numpy as np


def creer_image(longueur,largeur):
	display = np.zeros((longueur,largeur,3))
	return display

def bouger_image(longueur,largeur,pos):
	display = creer_image(longueur,largeur)
	display[pos[0],pos[1]] = [0,0,255]

	cv2.imshow("Test",display)
	key = cv2.waitKey(int(1000/12))
	return key,display

pos = [100,100]
display = bouger_image(200,200,pos)[1]
while True:
	display[pos[0],pos[1]] = [0,0,0]
	pos[0], pos[1] = pos[0] + 1, pos[1]
	display[pos[0],pos[1]] =  [0,0,255]
	key = cv2.waitKey(int(1000/12))
	if key == ord("z"):
		display[pos[0],pos[1]] = [0,0,0]
		pos = [pos[0] - 1, pos[0]]
		display[pos[0], pos[1]] = [0, 0, 255]
		cv2.imshow("Test",display)
	if key == 13:
		print(key)
		break








