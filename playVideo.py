import cv2, sys

# VideoCapture() 클래스 객체 생성
cap = cv2.VideoCapture("output.avi")

frameSize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),\
      int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = int(cap.get(cv2.CAP_PROP_FPS))
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
delay = int(1000/fps)
print(fps)
print(frameCount)
while(True):
    retval, frame = cap.read()

    if not retval:
        break
    
    cv2.imshow('img',frame)
    if cv2.waitKey(delay)==27:
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()