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

import cv2, sys
import numpy as np
import os
import shutil
from glob import glob
from enum import Enum



class funcNum(Enum):
    resize = 1
    rotate = 2
    hflip  = 3
    vflip  = 4
    crop   = 5

class DataAug:
    def __init__(self, dataPath):
        self.dataPath = dataPath
        self.img = None
        self.imageName = None
        self.splitName = None
    
    def getFileList(self, dataPath):
        fileNames = glob(dataPath+'/*.jpg')
        return fileNames
    
    def readImg(self, image_path):
        self.img = cv2.imread(image_path)
        self.imageName = os.path.basename(image_path)
        self.splitName = os.path.splitext(self.imageName)[0]
        return self.img
            
    def dispImg(self):
        return self.img
    
    def resize(self,img=None,dsize=(224,224)):
        if img is None:
            dst = cv2.resize(self.img, dsize, interpolation=cv2.INTER_AREA)
        else:
            dst = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)
        
        savefileName = self.genFileName(funcNum.resize, 224)
        cv2.imwrite(savefileName,dst)
        return dst
            
    def rotate(self, img=None, multi=True, interAngle=20):
        h, w = img.shape[:2]
        # 튜플로 centerPt를 저장
        centerPt = (w/2, h/2)
        if multi:
            for angle in range(interAngle,360,interAngle):
                # getRotationMatrix2D가 알아서 변환행렬 만들어줌
                aff = cv2.getRotationMatrix2D(centerPt, angle, 1)
                dst = cv2.warpAffine(img, aff, (w, h))
                savefileName = self.genFileName(funcNum.rotate,angle)
                cv2.imwrite(savefileName,dst)
        else:
            aff = cv2.getRotationMatrix2D(centerPt, interAngle, 1)
            dst = cv2.warpAffine(img, aff, (w, h))
            savefileName = self.genFileName(funcNum.rotate,angle)
            cv2.imwrite(savefileName,dst)
            return dst
    
    def flip(self, img=None, hflip=True):
        if hflip:
            if img is None:
                dst = cv2.flip(self.img, 1)
            else:
                dst = cv2.flip(img, 1)
            savefileName = self.genFileName(funcNum.hflip)
            cv2.imwrite(savefileName,dst)            
        else:
            if hflip:
                dst = cv2.flip(img, 1)
            else:
                dst = cv2.flip(img, 0)
                
            savefileName = self.genFileName(funcNum.vflip)
            cv2.imwrite(savefileName,dst)
        return dst               

    def createClassFolder(self, classNames, exist_ok=False):
        for Name in classNames:
            classPath = os.path.join(dataPath, Name)
            
            if not exist_ok:
                shutil.rmtree(classPath)
            
            # 클래스별 폴더를 생성한다.
            os.makedirs(classPath,exist_ok=exist_ok)

    def genFileName(self,procName,value=None):
        if procName==funcNum.resize:
            fileName = self.splitName + '_resize_' + str(value) +'.jpg'
            className = self.splitName.split('_')[0]
            saveName = os.path.join(self.dataPath,className,fileName)
            return saveName
        elif procName==funcNum.rotate:
            fileName = self.splitName + '_rot_' + str(value) +'.jpg'
            className = self.splitName.split('_')[0]
            saveName = os.path.join(self.dataPath,className,fileName)
            return saveName
        elif procName==funcNum.hflip:
            fileName = self.splitName + '_hflip.jpg'
            className = self.splitName.split('_')[0]
            saveName = os.path.join(self.dataPath,className,fileName)
            return saveName
        elif procName==funcNum.vflip:
            fileName = self.splitName + '_vflip.jpg'
            className = self.splitName.split('_')[0]
            saveName = os.path.join(self.dataPath,className,fileName)
            return saveName             


# 전역 변수
DEBUG = True

if __name__ == "__main__":

    # 현재 작업 폴더 기준 데이터 경로 설정
    dataPath = os.path.join(os.getcwd(), 'DataAug')
    # 원본 이미지 경로
    dataOrg = os.path.join(dataPath, 'org')
    # 클래스명은 아래와 같이 4개
    classNames = ['carKey', 'whitePen', 'blackPen', 'airPod']

    # 클래스 객체를 생성
    dataAug = DataAug(dataPath)
    # 클래스별 데이터 증식 폴더를 생성한다.
    exist_ok=False
    dataAug.createClassFolder(classNames,exist_ok)
    fileNames = dataAug.getFileList(dataOrg)

    # if DEBUG:
    #     for fileName in fileNames:
    #         print(fileName)
    
    
    inteAngle = 20  # rotate시 angle간격
    multi=True # rotate시 여러 장을 동시에 실행할지
    
    for fileName in fileNames:
        img = dataAug.readImg(fileName)
        img_resize = dataAug.resize()

        dataAug.rotate(img_resize, multi, inteAngle)
        dataAug.flip(img_resize,hflip=True)
        dataAug.flip(img_resize,hflip=False)





