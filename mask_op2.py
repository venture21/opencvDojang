import cv2, sys

#이미지 불러오기
# 대상이미지 cat.bmp
dst = cv2.imread('data2/cat.bmp')
# src이미지에 logo를 오려서 붙이기
# png파일을 읽을때는 cv2.IMREAD_UNCHANGED 적용필요!!
logo = cv2.imread('data2/opencv-logo-white.png',cv2.IMREAD_UNCHANGED)

# 파일이 정상적으로 읽히지 않았다면
if dst is None or logo is None:
    sys.exit("Image Load failed!")

# logo에서 알파채널만 가져오기
mask = logo[:,:,3]

# logo에서 BGR채널 가져오기
src = logo[:,:,:-1]


# 마스크의 크기만큼만 오려서 src에 적용
h,w = mask.shape[:2]
crop = dst[10:10+h, 10:10+w]


# 마스크 연산은 마스크 크기 만큼만
# crop은 src배열을 부르는 또 따른 이름
cv2.copyTo(src,mask,crop)
cv2.imshow('dst',dst)
cv2.imshow('src',src)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()

