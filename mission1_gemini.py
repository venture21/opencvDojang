import cv2
import numpy as np

def reduce_low_light_noise(image_path):
    """
    저조도 이미지의 노이즈를 줄입니다.

    Args:
        image_path (str): 이미지 파일 경로

    Returns:
        numpy.ndarray: 노이즈가 줄어든 이미지
    """

    src = cv2.imread(image_path)

    if src is None:
        print('Image load failed!')
        return

    # 밝기 조절 (gamma correction)
    gamma = 1.5  # 조절값 (1보다 크면 밝아짐, 작으면 어두워짐)
    look_up_table = np.empty((1, 256), np.uint8)
    for i in range(256):
        look_up_table[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    src = cv2.LUT(src, look_up_table)

    # 노이즈 제거 1: Bilateral Filtering (색상 경계 보존)
    dst1 = cv2.bilateralFilter(src, -1, 10, 5)

    # 노이즈 제거 2: Fast Non-Local Means Denoising (색상 고려)
    dst2 = cv2.fastNlMeansDenoisingColored(dst1, None, 10, 10, 7, 21)
    dst3 = cv2.fastNlMeansDenoisingColored(src, None, 10, 10, 7, 21)

    return dst2, dst3

# 이미지 경로 설정
image_path = 'mission/01.png'  

# 노이즈 제거 함수 호출
denoised_image, dst3 = reduce_low_light_noise(image_path)

# 결과 이미지 출력
cv2.imshow('Original', cv2.imread(image_path))
cv2.imshow('Denoised', denoised_image)
cv2.imshow('only fastNlMeansDenoisingColored', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()