# inRange함수를 잘 설정하려면 trackBar기능이 필요하다.
import sys
import numpy as np
import cv2

# 트랙바 콜백 함수 생성
def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'Trackbar')
    hmax = cv2.getTrackbarPos('H_max', 'Trackbar')
    smin = cv2.getTrackbarPos('S_min', 'Trackbar')
    smax = cv2.getTrackbarPos('S_max', 'Trackbar')
    vmin = cv2.getTrackbarPos('V_min', 'Trackbar')
    vmax = cv2.getTrackbarPos('V_max', 'Trackbar')
    
    # inRange함수에 적용
    dst = cv2.inRange(src_hsv, (hmin,smin,vmin), (hmax,smax,vmax))
    cv2.imshow('Trackbar', dst)
    
    # # red검출 inRange
    # mask_red1 = cv2.inRange(src_hsv,(0,100,0), (10,255,255))
    # mask_red2 = cv2.inRange(src_hsv,(160,100,0), (180,255,255))
    # mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    # #yellow검출 inRange
    # mask_yellow = cv2.inRange(src_hsv,(15,100,0), (35,255,255))

    # #green검출 inRange
    # mask_green = cv2.inRange(src_hsv,(50,100,0), (75,255,255))
    # green_pixels = cv2.countNonZero(mask_green)
    # red_pixels = cv2.countNonZero(mask_red2)
    # yellow_pixels = cv2.countNonZero(mask_yellow)
    # print("g_count : ", green_pixels)
    # print("r_count : ", red_pixels)
    # print("y_count : ", yellow_pixels)
    
    # # 딕셔너리를 사용하여 색상과 픽셀 수 연결
    # color_pixels = {
    #     "red": red_pixels,
    #     "yellow": yellow_pixels,
    #     "green": green_pixels,
    # }

    # # 가장 많은 픽셀 수를 가진 색상 찾기
    # max_color = max(color_pixels, key=color_pixels.get)

    # # 결과 출력
    # print(max_color)
    #     

#fileName = 'data2/candies.png'
fileName = 'data2/HSV_cylinder.jpg'
#fileName = 'data2/red.jpg'
#fileName = 'data2/green.jpg'
#fileName = 'data2/yellow.jpg'

src = cv2.imread(fileName)

if src is None:
    sys.exit("Image Load failed!")
    
# 색상의 범위를 잘 지정하려면 bgr->hsv
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# 창에 트랙바를 넣기 위해서는 창을 먼저 생성
cv2.namedWindow('Trackbar')

cv2.imshow('Trackbar', src_hsv)

# 트랙바 생성 : 'H_min' 트랙바의 이름, 범위 0~255,  
# on_trackbar : 트랙바를 움직일때 호출되는 함수(콜백함수)
cv2.createTrackbar('H_min', 'Trackbar', 0, 180, on_trackbar)
cv2.createTrackbar('H_max', 'Trackbar', 0, 180, on_trackbar)
cv2.createTrackbar('S_min', 'Trackbar', 0, 255, on_trackbar)
cv2.createTrackbar('S_max', 'Trackbar', 0, 255, on_trackbar)
cv2.createTrackbar('V_min', 'Trackbar', 0, 255, on_trackbar)
cv2.createTrackbar('V_max', 'Trackbar', 0, 255, on_trackbar)
on_trackbar(0)

cv2.waitKey()
cv2.destroyAllWindows()


