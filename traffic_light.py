import cv2
import numpy as np

def detect_traffic_light_color(image_path):
    """
    이미지에서 신호등 색상을 감지합니다.

    Args:
        image_path: 이미지 파일 경로

    Returns:
        감지된 신호등 색상 (str): "red", "yellow", "green" 또는 "unknown"
    """
    # 이미지 로드
    image = cv2.imread(image_path)

    # BGR에서 HSV 색상 공간으로 변환
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 각 색상에 대한 HSV 임계값 정의
    red_lower1 = np.array([0, 100, 100])
    red_upper1 = np.array([10, 255, 255])
    red_lower2 = np.array([160, 100, 100])
    red_upper2 = np.array([180, 255, 255])

    yellow_lower = np.array([15, 100, 100])
    yellow_upper = np.array([35, 255, 255])

    green_lower = np.array([40, 50, 50])
    green_upper = np.array([80, 255, 255])

    # inRange 함수를 사용하여 각 색상 범위 내의 픽셀 마스크 생성
    mask_red1 = cv2.inRange(hsv, red_lower1, red_upper1)
    mask_red2 = cv2.inRange(hsv, red_lower2, red_upper2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    mask_green = cv2.inRange(hsv, green_lower, green_upper)

    # 각 마스크의 흰색 픽셀 수 계산
    red_pixels = cv2.countNonZero(mask_red)
    yellow_pixels = cv2.countNonZero(mask_yellow)
    green_pixels = cv2.countNonZero(mask_green)

    # 가장 많은 흰색 픽셀을 가진 색상을 신호등 색상으로 결정
    if red_pixels > yellow_pixels and red_pixels > green_pixels:
        return "red"
    elif yellow_pixels > red_pixels and yellow_pixels > green_pixels:
        return "yellow"
    elif green_pixels > red_pixels and green_pixels > yellow_pixels:
        return "green"
    else:
        return "unknown"

# 예시 이미지 경로 (본인 이미지 경로로 변경)
image_path = "data2/green.jpg"

# 신호등 색상 감지 및 출력
color = detect_traffic_light_color(image_path)
print(f"신호등 색상: {color}")