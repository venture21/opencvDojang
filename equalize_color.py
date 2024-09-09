import cv2

# 컬러 이미지 불러오기
image = cv2.imread('mission/01.png')

# YCrCb 색 공간으로 변환
ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# 채널 분리
y, cr, cb = cv2.split(ycrcb_image)

# Y 채널에 히스토그램 평활화 적용
y = cv2.src_norm = cv2.normalize(y, None, 0, 255, cv2.NORM_MINMAX)

# 채널 병합
merged_ycrcb = cv2.merge((y, cr, cb))

# BGR 색 공간으로 변환
equalized_image = cv2.cvtColor(merged_ycrcb, cv2.COLOR_YCrCb2BGR)

# 이미지 표시 (선택 사항)
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()