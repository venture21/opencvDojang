import threading
import time

# 합을 저장할 변수, lock 객체 생성
sum_of_numbers = 0
lock = threading.Lock()

# 스레드 함수: 주어진 범위의 숫자 합을 계산
def calculate_sum(start, end):
    global sum_of_numbers
    local_sum = 0
    for i in range(start, end + 1):
        local_sum += i
    # lock을 얻은 후, 전역 변수에 값을 더하고 lock을 해제
    with lock:
        sum_of_numbers += local_sum

start_time = time.time()  # 시작 시간 기록

# 스레드 생성 및 시작
thread1 = threading.Thread(target=calculate_sum, args=(1, 50000000))
thread2 = threading.Thread(target=calculate_sum, args=(50000001, 100000000))
thread1.start()
thread2.start()

# 스레드가 종료될 때까지 대기
thread1.join()
thread2.join()

end_time = time.time()  # 종료 시간 기록
execution_time = end_time - start_time  # 실행 시간 계산

print(f"1부터 100000000까지의 합: {sum_of_numbers}")
print(f"실행 시간: {execution_time:.6f} 초")