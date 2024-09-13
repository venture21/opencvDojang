import cv2, sys
import numpy as np
from glob import glob
import os

# 0. 파일 목록 읽기(data폴더) *.jpg -> 리스트 
# 1. 이미지 불러오기
# 2. 마우스 콜백함수 생성
# 3. 콜백함수안에서 박스를 그리고, 박스 좌표를 뽑아낸다. (마우스 좌표 2개)
#    참고로 YOLO에서는 박스의 중심좌표(x,y), w,h
# 4. 이미지파일명과 동일한 파일명으로(확장자만 떼고) txt파일 생성
# 추가 기능0 : 박스를 잘못 쳤을때 'c'를 누르면 현재파일의 박스 내용 초기화
# 추가 기능1 : 화살표(->)를 누르면 다음 이미지 로딩되고(1~4)
# 추가 기능2 : 화살표(<-)를 눌렀을때 txt파일이 있다면 박스를 이미지 위에 띄워주면

def getImageList():
    # 현재 작업 디렉토리 확인
    basePath = os.getcwd()
    dataPath = os.path.join(basePath,'images')
    fileNames = glob(os.path.join(dataPath,'*.jpg'))
    
    return fileNames

# corners : 좌표(startPt, endPt)
# 2개 좌표를 이용해서 직사각형 그리기
def drawROI(img, corners):
    # 박스를 그릴 레이어를 생성 : cpy
    cpy = img.copy()
    line_c = (128,128,255) #직선의 색상
    lineWidth = 2
    for corners in boxList:
        #print("corners:{}".format(corners))
        cv2.rectangle(cpy, tuple(corners[0]), tuple(corners[1]), color=line_c, thickness=lineWidth)

    # alpha=0.3, beta=0.7, gamma=0
    disp = cv2.addWeighted(img,0.3,cpy,0.7,0)
    return disp

#  마우스 콜백 함수 정의
def onMouse(event, x, y, flags, param):
    global startPt, img, ptList, cpy, txtWrData, boxList
    if event == cv2.EVENT_LBUTTONDOWN:
        startPt=(x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        ptList = [startPt,(x,y)]
        boxList.append(ptList)
        print(boxList)
        txtWrData = str(ptList)
        cpy = drawROI(img, boxList)

        startPt = None
        cv2.imshow('label',cpy)
    elif event == cv2.EVENT_MOUSEMOVE:
        if startPt:
            ptList=[startPt, (x,y)]
            boxList.append(ptList)
            cpy = drawROI(img, boxList)
            boxList.pop()
            cv2.imshow('label',cpy)

ptList=[]
startPt=None
cpy=[]
txtWrData = ""
boxList=[]

fileNames = getImageList()

img = cv2.imread(fileNames[0])

cv2.namedWindow('label')
cv2.setMouseCallback('label',onMouse,[img])
cv2.imshow('label', img)

while True:
    key = cv2.waitKey()
    if key==27:
        break
    elif key==ord('s'):
        filename, ext = os.path.splitext(fileNames[0])
        txtFilename = filename + '.txt'
        f = open(txtFilename,'w')
        f.write(txtWrData)
        f.close()
        #print("before write txt :{}".format(txtWrData))
        

cv2.destroyAllWindows()
