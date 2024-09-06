import cv2
import threading
import time
from datetime import datetime


# 1분 타이머 스레드 함수
def timer_thread(stop_event):
    global recording
    
    for i in range(rec_length):
        while recording:
            time.sleep(1)
    
    stop_event.set()


# 폴더 생성 함수
def makeFolder(now):
    now = datetime.now()
    folderName = now.strftime("%Y%m%d_%H%M분")


#global 변수
recording = True
rec_length = 60  # 녹화 시간 (초)
key = None

def main():
    # 웹캠 캡처 객체 생성
    #fileName = "C:/Users/SBA/opencvDojang/video.mp4"
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    #cap = cv2.VideoCapture(fileName)

        
    # 녹화 설정
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # 프레임 레이트 설정
    segment_count = 1
    

    while True:
        stop_recording = threading.Event()
        timer = threading.Thread(target=timer_thread, args=(stop_recording,))
        timer.start()
        recording = True
        out = cv2.VideoWriter("C:/Users/SBA/test/output{}.avi".format(segment_count), fourcc, fps, (width, height))  # 출력 파일 설정

    # 녹화 시작 

        while recording:
            ret, frame = cap.read()
            if not ret:
                recording = False  # 영상이 끝나면 녹화 중지
                break

            out.write(frame)
            cv2.imshow('blackbox', frame)
            key = cv2.waitKey(20)
            if  key == 27:
                recording = False  # 'Esc' 키 누르면 녹화 중지
                break

            if stop_recording.is_set():
                recording = False  # 타이머 완료 시 녹화 중지
                
        
        out.release()
        #timer.join()
        segment_count += 1
        
        if key == 27 or not ret:
            recording = False
            break

    timer.join(timeout=0)
    cap.release()
    cv2.destroyAllWindows()
    
# 이 파일이 직접실행될때
if __name__ == "__main__":
    main()
