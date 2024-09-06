# 블랙박스 만들기

# 1. 60초에 동영상 한개가 생성되도록 한다.
# 파일명은 20240902-161903.avi

# 2. 폴더 생성은 날짜+현재시간
# 20240902-16 00분 ~ 59분
# 한시간마다 폴더 생성

# 3. 블랙박스 녹화 폴더가 500MB이면 가장 오래된 녹화 폴더 삭제 

# 4. Thread 적용하여 record_time변수의 값과 실제 녹화영상의 길이가 같도록 한다. 



# updated 0904

# 리팩토링 예정 
# - 용량 확인하는 주기를 설정(큰 용량을 관리할 경우 성능저하)
# - 객체 생성 및 영상저장 생성자 메서드추가 
# - 최신 파일을 확인할때 인덱스로 검색하지 않고 함수로 변경예정 


import cv2, sys
import time
from datetime import datetime
import os
from os.path import join, getsize
import schedule
import threading


record_time = 60 # 녹화시간

# 파일명 만들어주는 함수가 필요 
def create_filename():
    # 파일명으로 사용할 현재시각 불러오기 
    now = datetime.now()
    filename = now.strftime('%Y%m%d-%H%M%S') + '.avi'
    return filename

def make_folder(folder_path):
    now = datetime.now()
    folder_name = now.strftime('%Y%m%d' + '-' + str(now.hour) + '시')
    # 한시간에 한번 폴더생성 함수가 실행되도록 
    schedule.every().hour.do(make_folder)
    # 폴더 중복생성 확인
    if not os.path.exists(os.path.join(folder_path,folder_name)):
        os.makedirs(os.path.join(folder_path,folder_name))
        print(f"'{folder_name}' 폴더가 생성되었습니다.")

# 최신 폴더 확인
def latestFolderCheck():
    latest_folder = max(os.listdir(folder_path), key=lambda f: os.path.getctime(os.path.join(folder_path, f)))
    return latest_folder

# videoCapture 클래스 객체 생성 및 호출 
# cap = cv2.VideoCapture(0)
# 영상녹화가 늦어지는 점 개선
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# 크기 조절
cap.set(cv2.CAP_PROP_FRAME_WIDTH,300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,200)
cap.set(cv2.CAP_PROP_FPS, 30)
# FPS 가져오기
fps = cap.get(cv2.CAP_PROP_FPS)


def timer_thread(stop_event):
    global running
    for _ in range(record_time):
        if not running:  # running이 False이면 바로 종료
            break
        time.sleep(1)
    stop_event.set()  # 이벤트 설정 (녹화 중지)


# 파일을 직접 실행 시 메인 함수부터 실행됨 
# 명시적으로 지정해두는 것이 가독성도 좋다.
if __name__ == "__main__":
    running = True
    while(True):
        # 녹화 중지 이벤트 생성
        stop_recording = threading.Event()

        # 타이머 스레드 생성 및 시작
        timer = threading.Thread(target=timer_thread, args=(stop_recording,))
        timer.start()
        
        # 녹화 파일명 만들기
        create_filename()

        folder_path = 'C:/Users/user/Desktop/REPOSITORY/opencvDojang/blackbox'
        
        # 폴더생성
        # 프로그램 실행 상태일때 한시간에 한번씩 생성
        make_folder(folder_path)
        
        # 영상 저장할때는 프레임 사이즈도 읽어온다.
        framesize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        # 코덱설정
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # 영상저장 생성자
        output_path = os.path.join(folder_path, latestFolderCheck(), create_filename())
        out = cv2.VideoWriter(output_path + create_filename(), fourcc, fps, framesize)
        print(framesize)

        recording = True
        while recording:
            ret,frame = cap.read()
            if not ret:
                break

            out.write(frame)
            cv2.imshow('blackbox', frame)

            key = cv2.waitKey(30)
            if key == ord('q'):
                # terminate_thread(timer)
                break
            # 타이머 이벤트 확인 (1분 경과 여부)
            if stop_recording.is_set():
                recording = False
        
        if key == ord('q'):
            running = False
            timer.join(timeout=0)
            

        # 3. 현재 폴더의 용량이 500mb가 되면 가장 오래된 파일 지우기 
        # 용량 확인 주기 추가해야함 
        
        # os.listdir 함수
        new_path = os.path.join(folder_path, latestFolderCheck())   # blackbox 폴더의 하위 폴더로 시간별 폴더를 생성했기 때문에 두 폴더를 결합해 하위폴더 경로를 만든다.
        max_size = 500  #500MB
        
        # blackbox 폴더의 하위폴더로 진입해 모든 파일의 용량을 더해주는 코드
        for name in os.listdir(new_path):
            # 1MB는 1024 * 1024 바이트이므로, 이를 나누어 바이트를 MB로 변환
            folder_size = sum([getsize(join(new_path, name)) for name in os.listdir(new_path)]) / (1024.0 * 1024.0)
            if folder_size > max_size:
                # 가장 최신 파일을 삭제 : 최신파일을 리스트의 0번째 인덱스로 지정했는데 이 부분도 함수를 사용하여 수정할 필요가 있어보임
                oldest_file = os.listdir(new_path)[0]
                os.remove(new_path+ '/' + oldest_file)

        if key == ord('q'):
            break
        

    out.release()
    cap.release()
    cv2.destroyAllWindows()