import cv2
import threading
import time

# 1분 타이머 스레드 함수
def timer_thread(stop_event):
    global recording
    time.sleep(60)  # 60초 (1분) 대기
    stop_event.set()  # 이벤트 설정 (녹화 중지)

# 녹화 중지 이벤트 생성
stop_recording = threading.Event()

# 타이머 스레드 생성 및 시작
timer = threading.Thread(target=timer_thread, args=(stop_recording,))
timer.start()

# 웹캠 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 녹화 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))  # 프레임 레이트 설정
print(fps)
out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))  # 출력 파일 설정

# 녹화 시작
recording = True
while recording:
    ret, frame = cap.read()  # 프레임 읽기
    if ret:
        out.write(frame)  # 프레임 저장
        cv2.imshow('Webcam Recording', frame)  # 미리보기 표시

        # 'q' 키를 누르면 즉시 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            recording = False
            break

    # 타이머 이벤트 확인 (1분 경과 여부)
    if stop_recording.is_set():
        recording = False

# 녹화 종료
cap.release()
out.release()
cv2.destroyAllWindows()