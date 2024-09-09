# cv2.normalize

import cv2, sys
import numpy as np

# grayscale로 읽어오기
src = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')
    
# src이미지에서 최소값과 최대값을 확인
pixMin, pixMax, _, _ = cv2.minMaxLoc(src)
#print(pixMin, pixMax)

# 이미지를 정규화 한다 0~255
dst = cv2.normalize(src,None, 0, 255, cv2.NORM_MINMAX) 
pixMin, pixMax, _, _ = cv2.minMaxLoc(dst)
print(pixMin, pixMax)
# 데이터 결과를 파일로 저장
cv2.imwrite('data2/Hawkes_norm.jpg', dst)
cv2.imshow('img', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

