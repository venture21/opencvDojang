import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

isColor = False

if not isColor:
    src1 = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('data2/Hawkes_norm.jpg', cv2.IMREAD_GRAYSCALE)

    if src1 is None or src2 is None:
        sys.exit('Image load failed')

    # 히스토그램을 만들기
    hist1 = cv2.calcHist([src1], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([src2], [0], None, [256], [0,256])
    plt.plot(hist1)
    plt.plot(hist2)
    min,max,_,_ = cv2.minMaxLoc(src1)
    print(min,max)
    min,max,_,_ = cv2.minMaxLoc(src2)
    print(min,max)

if isColor:
    src = cv2.imread('data/lena.bmp')
    
    if src is None:
        sys.exit("Image Load failed")

    #컬러 채널 분리
    colors = ['b','g','r']
    bgr_planes = cv2.split(src)
  
    for (p, c) in zip(bgr_planes, colors):
        hist = cv2.calcHist([p],[0],None,[256],[0,256])
        print(hist.shape)
        plt.plot(hist, color=c)

if not isColor:
    cv2.imshow('src',src1)
    cv2.imshow('src2',src2)

if isColor:
    cv2.imshow('src',src)

# matplotlib 띄우기
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()



