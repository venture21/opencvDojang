import threading
import time

# 각 스레드의 결과를 저장할 리스트
thread_results = [0, 0] 

# 스레드 함수: 주어진 범위의 숫자 합을 계산하여 thread_results에 저장
def calculate_sum(start, end, thread_index):
    local_sum = 0
    for i in range(start, end + 1):
        local_sum += i
    thread_results[thread_index] = local_sum

start_time = time.time()  # 시작 시간 기록

# 스레드 생성 및 시작
thread1 = threading.Thread(target=calculate_sum, args=(1, 50000000, 0))  # thread_index 0
thread2 = threading.Thread(target=calculate_sum, args=(50000001, 100000000, 1)) # thread_index 1
thread1.start()
thread2.start()

# 스레드가 종료될 때까지 대기
thread1.join()
thread2.join()

# 두 스레드의 결과를 합산
total_sum = sum(thread_results)

end_time = time.time()  # 종료 시간 기록
execution_time = end_time - start_time  # 실행 시간 계산

print(f"1부터 100000000까지의 합: {total_sum}")
print(f"실행 시간: {execution_time:.6f} 초")