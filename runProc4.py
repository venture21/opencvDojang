import multiprocessing
import time

# 프로세스 함수 정의
def sum_numbers(start, end, queue):
    total = 0
    for i in range(start, end + 1):
        total += i
    queue.put(total)

if __name__ == '__main__':
    start_time = time.time()  # 시간 측정 시작

    # 멀티프로세싱 큐 생성
    queue = multiprocessing.Queue()

    # 프로세스 개수 설정
    num_processes = 4

    # 각 프로세스가 담당할 데이터 범위 계산
    chunk_size = 100000000 // num_processes

    # 프로세스 생성 및 시작
    processes = []
    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size
        if i == num_processes - 1:  # 마지막 프로세스는 나머지 처리
            end = 100000000
        p = multiprocessing.Process(target=sum_numbers, args=(start, end, queue))
        processes.append(p)
        p.start()

    # 모든 프로세스가 완료될 때까지 대기
    for p in processes:
        p.join()

    # 결과를 큐에서 가져와 합산
    total_sum = 0
    for _ in range(num_processes):
        total_sum += queue.get()

    end_time = time.time()  # 시간 측정 종료
    execution_time = end_time - start_time

    # 결과 출력
    print("1부터 100000000까지의 합:", total_sum)
    print(f"실행 시간: {execution_time:.6f} 초")