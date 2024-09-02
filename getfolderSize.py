import os

def get_folder_size(folder_path):
    """
    특정 폴더의 디스크 사용량을 계산하는 함수

    Args:
        folder_path (str): 디스크 사용량을 계산할 폴더 경로

    Returns:
        int: 폴더의 총 크기 (바이트)
    """

    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # 오류 처리: 파일이 존재하지 않거나 접근할 수 없는 경우 건너뜁니다.
            try:
                total_size += os.path.getsize(fp)
            except FileNotFoundError:
                print(f"파일을 찾을 수 없습니다: {fp}")
            except PermissionError:
                print(f"파일에 접근할 수 없습니다: {fp}")
    return total_size

if __name__ == "__main__":
    folder_path = 'C:/Users/park0/opencvDojang/data'
    total_size = get_folder_size(folder_path)

    # 바이트 단위 출력
    print(f"폴더 '{folder_path}'의 총 크기: {total_size} 바이트")

    # KB, MB, GB 단위 변환
    if total_size >= 1024:
        total_size_kb = total_size / 1024
        print(f"폴더 '{folder_path}'의 총 크기: {total_size_kb:.2f} KB")
        if total_size_kb >= 1024:
            total_size_mb = total_size_kb / 1024
            print(f"폴더 '{folder_path}'의 총 크기: {total_size_mb:.2f} MB")
            if total_size_mb >= 1024:
                total_size_gb = total_size_mb / 1024
                print(f"폴더 '{folder_path}'의 총 크기: {total_size_gb:.2f} GB")