import os

# 순회할 루트 폴더 경로
folder_path = "C:/Users/park0/opencvDojang/ex1"

# os.walk() 함수를 사용하여 폴더 트리 순회
for dirpath, dirnames, filenames in os.walk(folder_path):
    # 현재 폴더 경로 출력
    print(f"현재 폴더: {dirpath}")

    # 현재 폴더 내의 하위 폴더 목록 출력
    print(f"하위 폴더: {dirnames}")

    # 현재 폴더 내의 파일 목록 출력
    print(f"파일: {filenames}")

    print("-" * 30)  # 구분선 출력