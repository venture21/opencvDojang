import cv2
import numpy as np

src1 = cv2.imread('data2/airplane.bmp')
src2 = cv2.imread('data2/field.bmp')

alpha = 0.8
beta = 1 - alpha

dst1 = cv2.addWeighted(src1, alpha=alpha, src2=src2, beta=beta, gamma=0)

cv2.imshow('img1', src1)
cv2.imshow('img2', src2)
cv2.imshow('dst1',dst1)
cv2.waitKey()
cv2.destroyAllWindows()
 