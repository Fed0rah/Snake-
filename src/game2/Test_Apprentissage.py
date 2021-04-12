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

pos = [1000,1000]
display = bouger_image(2000,2000,pos)[1]

#display[pos[0],pos[1]] = [0,0,0]
#pos[0], pos[1] = pos[0] + 1, pos[1]
for i in range(pos[0] - 25,pos[1] + 26):
	for j in range(pos[1] - 25,pos[1] + 26):
		display[i,j] =  [0,0,255]
while True:
	cv2.imshow("Test", display)
	key = cv2.waitKey(int(100/12))
	#if key == ord("z"):
	for i in range(pos[0] - 25,pos[0] + 26):
		for j in range(pos[1] - 25,pos[1]+ 26):
			display[i,j] = [0,0,0]
	pos = [pos[0] , pos[1] + 50]
	for i in range(pos[0] - 25,pos[0] + 26):
		for j in range(pos[1] - 25,pos[1] + 26):
			display[i,j] = [0, 0, 255]





	if key == 13:
		print(key)
		break








