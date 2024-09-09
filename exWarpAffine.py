import cv2, sys
import numpy as np

def translate(src, x_move=0,y_move=0):
    # 이미지의 이동 변환 x->200, y->100만큼 이동
    # 이동 변환 행렬
    aff = np.array([[1, 0, x_move],[0, 1, y_move]], dtype=np.float32)
    dst = cv2.warpAffine(src, aff, (0,0))
    return dst

def shear(src, x_shear=0,y_shear=0):
    if x_shear>0 and y_shear==0:
        aff = np.array([[1, x_shear, 0],[0, 1, 0]], dtype=np.float32)
        h, w = src.shape[:2]
        dst = cv2.warpAffine(src,aff, (w + int(h * x_shear), h))
    elif y_shear>0 and x_shear==0:
        aff = np.array([[1, 0, 0],[y_shear, 1, 0]], dtype=np.float32)
        h, w = src.shape[:2]
        dst = cv2.warpAffine(src,aff, (w, h+int(w * y_shear)))    
    
    return dst


def scale(src, x_scale,y_scale):
    h, w = src.shape[:2]
    aff = np.array([[x_scale, 0, 0],[0, y_scale, 0]], dtype=np.float32)
    dst = cv2.warpAffine(src,aff, (int(w*x_scale), int(h*y_scale)))
    return dst

src = cv2.imread('data/lenna.bmp')

if src is None:
    sys.exit('Image load failed')

print(src.shape)
#dst = translate(src,50,50)
dst = shear(src, 0, 0.5)
#dst = scale(src, 1.5, 1.5)
# 512x512 -> 1024x1024 해상도로 설정
#dst = cv2.resize(src,(1024,1024))
# 비율로 설정(해상도입력X)
#dst = cv2.resize(src,(0,0), fx=1.5,fy=1.5) 

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()
    
