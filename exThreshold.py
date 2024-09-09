import cv2, sys
import matplotlib.pyplot as plt
import myLib

# 이미지 불러오기
src = cv2.imread('data2/apple_th.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')

myLib.hist_gray(src)

# threshold함수를 이용해서 흑과 백으로 나눈다.
ret, src_th = cv2.threshold(src, 230, 255, cv2.THRESH_BINARY)
print(ret)
cv2.imshow('src',src)
cv2.imshow('src_th',src_th)
cv2.waitKey()
cv2.destroyAllWindows() 