import cv2, sys
import numpy as np


# 마우스 콜백 함수 구현
# 마우스에서 이벤트가 발생하면서 호출되는 함수
# 버튼 클릭, 마우스 좌표를 이동
def mouse_callback(event, x, y, flags, param):
    global img
    
    if event==cv2.EVENT_LBUTTONDOWN:
        print("LButton Down!")
    elif event==cv2.EVENT_LBUTTONUP:
        print("LButton UP!")
    elif event==cv2.EVENT_MOUSEMOVE:
        print("x:{},y:{}".format(x,y))
    



# 흰색 캔버스를 생성
#img = np.zeros((512,512,3), np.uint8)+255
img = np.ones((512,512,3), np.uint8)*255 
cv2.namedWindow('img')
#메인에서 setMouseCallback함수를 실행하면서 콜백함수를 지정
cv2.setMouseCallback('img', mouse_callback,[img] )
cv2.imshow('img',img)

cv2.waitKey()
cv2.destroyAllWindows()


