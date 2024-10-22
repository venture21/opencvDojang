# 1. 배경 : 흰색 책상, 우드 테이블
# 2. 데이터 증식 조건 
#    2.0 스마트폰으로 사진 촬영후 이미지 크기를 줄여주자. (이미지 크기 224x224)
#        대상물 촬영을 어떻게 해야할지 확인
#    2.1 rotate : 회전(10~30도)범위 안에서 어느 정도 각도를 넣어야 인식이 잘되는가?
#    2.2 hflip, vflip : 도움이 되는가? 넣을 것인가?
#    2.3 resize, crop : 가능하면 적용해 보자.
#    2.4 파일명을 다르게 저장 cf) jelly_wood.jpg, jelly_white.jpg
#        jelly_wood_rot_15.jpg, jelly_wood_hflip.jpg,jelly_wood_resize.jpg 
#    2.5 클래스 별로 폴더를 생성
#    2.6 데이터를 어떻게 넣느냐에 따라 어떻게 동작되는지 1~2줄로 요약

# 구성 순서 
# 1. 촬영한다.
# 2. 이미지를 컴퓨터로 복사, resize한다.
# 3. 육안으로 확인, 이렇게 사용해도 되는가?
# 4. 함수들을 만든다. resize, rotate, hflip, vflip, crop, 
#    원본파일명을 읽어서 파일명을 생성하는 기능은 모든 함수에 있어야 한다.(함수)
# 5. 단일 함수들 검증
# 6. 함수를 활용해서 기능 구현
# 7. 테스트(경우의수)
# 8. 데이터셋을 teachable machine사이트에 올려서 테스트
# 9. 인식이 잘 안되는 케이스를 분석하고 케이스 추가 1~8에서 구현된 기능을 이용

# 함수 스타일로 코딩
import cv2, sys
import numpy as np
import os
from glob import glob
import shutil
from enum import Enum

# 클래스에 내장될 기능을 번호로 설정
class funcNum(Enum):
    resize = 1
    rotate = 2
    hflip  = 3
    vflip  = 4
    crop   = 5

dataPath = os.path.join(os.getcwd(), 'DataAug')
dataOrg = os.path.join(dataPath, 'org')

#전역 변수 
DEBUG = False
dsize = (224,224)

# input  : dataPath
# output : dataPath안에 jpg파일의 리스트를 가져오기
# 확장하려면  기능추가 : img_type = ['jpg','png','gif']
def getFileList(dataPath):
    fileNames = glob(os.path.join(dataPath,'*.jpg'))
    if DEBUG:
        print(fileNames)
        
    if fileNames is None:
        print("fileList is empty!")
        
    return fileNames
    

# 이미지를 불러오는 함수
def readImg(image_path):
    img = cv2.imread(image_path)
    
    if img is None:
        sys.exit("Image Load Failed!")
    return img

# input  : 원본 파일명
# output : 새로생성될 파일명
def getFileName(imgName,func):
    if func==funcNum.resize:
        # 경로를 제외한 파일명만 올려낸다.
        baseName = os.path.basename(imgName)
        # 확장자만 분리
        baseNameSplit = os.path.splitext(baseName)[0]
        resizeName = baseNameSplit + '_resize_' + str(dsize[0]) + '.jpg'
        return resizeName

def resize(img=None, dsize=dsize,imgName=None):
    if img is None:
        print("image Path is None")
    
    dst = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)
    # 새로 만들 파일명 가져오기
    resizeName = getFileName(imgName, funcNum.resize)
    cv2.imwrite(resizeName,dst)
    return dst


classList = ['airPod','whitePen','blackPen','CarKey']

def createFolder():
    for classname in classList:
        # 기존에 폴더가 있으면 삭제하고, 새로 생성
        # 폴더안에 파일이 존재하더라도, 파일과 폴더를 모두 삭제
        classPath = os.path.join(dataPath,classname)
        print(classPath)
        # 폴더가 존재한다면
        if os.path.isdir(classPath):
            shutil.rmtree(classPath)
        os.makedirs(classPath,exist_ok=True)


def main():
    
    createFolder()
    fileNames = getFileList(dataOrg)
    print(len(fileNames))
    for fileName in fileNames:
        img = readImg(fileName)
        dst = resize(img,dsize,fileName)
        cv2.imshow('img',dst)
        cv2.waitKey()
        break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    




