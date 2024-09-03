import time

start_time = time.time()  # 시작 시간 기록

# 1부터 100000000까지의 합 계산
sum_of_numbers = sum(range(1, 100000001))

end_time = time.time()  # 종료 시간 기록
execution_time = end_time - start_time  # 실행 시간 계산

print(f"1부터 100000000까지의 합: {sum_of_numbers}")
print(f"실행 시간: {execution_time:.6f} 초")