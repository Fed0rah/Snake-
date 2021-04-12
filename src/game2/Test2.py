import cv2
import numpy as np

A1 = np.zeros((2000,2000,3))

Grid2 = np.zeros((40,40))
Grid2[20][20] = 1

def Update_Display(A,Grid):
	for i in range(len(Grid)):
		for j in range(len(Grid)):
			if Grid[i][j] == 1:
				for k1 in range(50*i,50*(i+1)):
					for k2 in range(50*j,50*(j+1)):
						print("ajout d'un pixel")
						A[k1][k2] = [0,0,255]

Update_Display(A1,Grid2)
cv2.imshow("Test",A1)
cv2.waitKey(0)