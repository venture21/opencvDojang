import cv2, sys
import numpy as np

src =cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')

kernel_size = 3
kernel = (kernel_size, kernel_size)

# blur처리
# 필터의 크기가  (3x3)
dst = cv2.blur(src, kernel = kernel)


cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()
