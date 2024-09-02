import sys
import cv2

# opencv 버전 확인
print('Hello OpenCV', cv2.__version__)

# imread('파일명') 이렇게 사용하고
# img의 데이터타입 numpy.ndarray
img_gray = cv2.imread('data/lenna.bmp', cv2.IMREAD_GRAYSCALE)
img_bgr  = cv2.imread('data/lenna.bmp')
# 파일을 못찾아서 이미지를 못 읽어온경우
# 프로그램 종료
if img_gray is None or img_bgr is None:
    print('Image load failed!')
    sys.exit()

# 창의 이름을 정의
cv2.namedWindow('image_gray',cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('image_bgr')
# 불러온 이미지를 창에 띄워준다.
# 'image'창에 읽어온 img 배열을 출력한다.
cv2.imshow('image_gray', img_gray)
cv2.imshow('image_bgr', img_bgr)
# 키입력을 기다리는 함수
# 함수 안에 값을 입력 단위 : ms
# waitKey함수에 지연값을 설정하지 않으면 무한대기
# 키보드 입력이 들어올때까지
cv2.waitKey()
# 모든 창을 다 닫는다.
cv2.destroyAllWindows()