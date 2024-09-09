import numpy as np
import cv2, sys
import matplotlib.pyplot as plt

def DisplayGrayHist(src):
    hist = cv2.calcHist([src], [0], None, [256], [0,256])
    plt.plot(hist)
    plt.show()

def DisplayColorHist(src):
    #컬러 채널 분리
    colors = ['b','g','r']
    bgr_planes = cv2.split(src)
  
    for (p, c) in zip(bgr_planes, colors):
        hist = cv2.calcHist([p],[0],None,[256],[0,256])
        print(hist.shape)
        plt.plot(hist, color=c)
    plt.show() 

def doNormalize(src):
    src_norm = cv2.normalize(src,None, 0, 255, cv2.NORM_MINMAX)     
    return src_norm

def doEqualize(src):
    dst = cv2.equalizeHist(src)
    return dst

src = cv2.imread('mission/01.png')

if src is None:
    sys.exit('Image Load Failed')

# YCrCb 색 공간으로 변환
ycrcb_image = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# 채널 분리
y, cr, cb = cv2.split(ycrcb_image)
y = cv2.src_norm = cv2.normalize(y, None, 0, 255, cv2.NORM_MINMAX)

y_norm = doNormalize(y)
y_equalize = doEqualize(y)
# DisplayGrayHist(y_norm)
# DisplayGrayHist(y_equalize)

y_mul = cv2.multiply(y, 1.5)
merged_mul = cv2.merge((y_mul, cr, cb))
merged_mul_bgr = cv2.cvtColor(merged_mul, cv2.COLOR_YCrCb2BGR)

merged_norm = cv2.merge((y_norm, cr, cb))
merged_norm_bgr = cv2.cvtColor(merged_norm, cv2.COLOR_YCrCb2BGR)

merged_equalize = cv2.merge((y_equalize, cr, cb))
merged_equalize_bgr = cv2.cvtColor(merged_equalize, cv2.COLOR_YCrCb2BGR)

DisplayColorHist(merged_norm_bgr)
DisplayColorHist(merged_mul_bgr)

# 이미지의 노이즈를 제거한다.
dst1 = cv2.medianBlur(merged_mul_bgr, 3)
dst2 = cv2.fastNlMeansDenoisingColored(merged_mul_bgr, None, 10, 10, 7, 18)

cv2.imshow('src',src)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)

cv2.waitKey()
cv2.destroyAllWindows()