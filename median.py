import cv2, sys
import numpy as np

src =cv2.imread('data2/noise.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')

dst = cv2.medianBlur(src, 3)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()
