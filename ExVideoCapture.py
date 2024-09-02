# 이미지를 불러올때는 imread()
# 동영상을 불러올때는 VideoCapture()

import cv2, sys

fileName = 'data/vtest.avi'

# VideoCapture 클래스 객체 생성 + 생성자가 호출(파일열기)
cap = cv2.VideoCapture(fileName)

# 동영상의 해상도 width, height 확인
frameSize = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), \
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(frameSize)

# 동영상 이미지를 다 가져올때까지 반복
while(True):
    # 동영상에서 한장의 이미지를 가져오기
    # retval : 동영상에서 이미지 가져올때 정상 동작 했나? True, False 
    # frame은 이미지 한장 
    # 동영상 코덱 디코딩도 포함
    retval, frame = cap.read()
    # retval가 양수가 아니면 while문 빠져나가기(종료)

    # False인 경우 if문이 실행
    if not retval:
        print(retval)
        break
    cv2.imshow('frame', frame)
    
    # 100ms대기 (이 동영상은 초당 10프레임 짜리니까)
    key = cv2.waitKey(100)
    # 키 입력이 ESC(27)이면 종료
    if key==27: # ESC
        break

# 동영상을 열었으면, 닫아야 한다.
if cap.isOpened():
    cap.release() # 열림 해제
    
cv2.destroyAllWindows()

