# 이미지 불러오기 : 동일
# opencv 패키지의 특성과 matplotlib 패키지의 특성의 차이를 이해
# 이미지 출력하기 : cv2.imshow() -> plt.imshow()

import cv2
import sys
from matplotlib import pyplot as plt

fileName = 'data/cat.jpg'

img = cv2.imread(fileName)

if img is None:
    sys.exit("Image Load is failed")

# opencv 모듈은 이미지를 읽어올때 컬러 스페이스의 순서
# B,G,R 
# 컬러 스페이스(채널 순서)를 바꿔주는 함수
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Matplotlib은 R,G,B로 사용
plt.imshow(imgRGB)
# matplotlib의 imshow에서 눈금을 표시 X
plt.axis('off')
plt.show()


