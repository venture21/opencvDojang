import cv2
import numpy as np

def enhance_image(image_path):
    """
    이미지에서 노이즈를 제거하고 건물에 선명도를 높입니다.

    Args:
        image_path (str): 이미지 파일 경로

    Returns:
        numpy.ndarray: 노이즈가 제거되고 선명도가 높아진 이미지
    """

    src = cv2.imread(image_path)

    if src is None:
        print('Image load failed!')
        return

    # 1. 노이즈 제거
    denoised = cv2.fastNlMeansDenoisingColored(src, None, 10, 10, 7, 21)

    # 2. 건물 영역 검출 (밝기를 기준으로 간단하게 검출)
    gray = cv2.cvtColor(denoised, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)  # 밝기 임계값 조절

    # 3. Sharpening 필터 생성
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])

    # 4. 마스크를 이용하여 건물 영역에만 Sharpening 적용
    sharpened = cv2.filter2D(denoised, -1, kernel)
    sharpened = cv2.bitwise_and(sharpened, sharpened, mask=mask)

    # 5. 노이즈 제거된 이미지와 선명하게 처리된 건물 합성
    result = denoised.copy()
    result[mask != 0] = sharpened[mask != 0]

    return result, mask

# 이미지 경로 설정
image_path = 'mission/03.png'  

# 이미지 향상 함수 호출
enhanced_image,mask = enhance_image(image_path)

# 결과 이미지 출력
cv2.imshow('Original', cv2.imread(image_path))
cv2.imshow('Enhanced', enhanced_image)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()