import cv2
import numpy as np

A = np.zeros((2000,2000,3))
pt_vert = [0,255,0]
for i in range(975,1025):
	for j in range(975,1025):
		A[i][j] = pt_vert
cv2.imshow("Test",A)
cv2.waitKey(0)

