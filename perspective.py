import cv2, sys
import numpy as np


#마우스 좌표를 얻기 위해 콜백함수 사용
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(x,y)
    
    cv2.imshow('img',img2)

img = cv2.imread('data2/book.jpg')

if img is None:
    sys.exit('Image load failed')
    
img2 = cv2.resize(img,(0,0),None,fx=0.5,fy=0.5)

w, h = img2.shape[1], img2.shape[0] 
print(w,h)

# 다각형의 좌표를 그릴때는 시계방향으로()
srcQuad = np.array([[256,152],[553,169],[443,565],[57,458]], np.float32)
# 변환될 좌표
dstQuad = np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]],np.float32)

# 변환 행렬 생성
pers = cv2.getPerspectiveTransform(srcQuad,dstQuad)
dst = cv2.warpPerspective(img2,pers,(w,h))

cv2.namedWindow('img')
#cv2.setMouseCallback('img', mouse_callback,[img2])
cv2.imshow('img',img2)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()
