import cv2
import numpy as np

# 마우스 클릭 이벤트를 처리할 함수
def draw_polygon(event, x, y, flags, param):
    global points, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing:
            # 클릭한 점이 첫 번째 점과 가까우면 다각형 완성
            if len(points) > 2 and cv2.norm(np.array([x, y]) - points[0]) < 10:
                drawing = False
                cv2.line(image, tuple(points[-1]), tuple(points[0]), (0, 0, 255), 2)
                cv2.fillPoly(image, [np.array(points, np.int32)], (0, 255, 0))
            else:
                # 그렇지 않으면 점 추가
                cv2.line(image, tuple(points[-1]), (x, y), (0, 0, 255), 2)
                points.append([x, y])
        else:
            # 새 다각형 시작
            drawing = True
            points = [[x, y]]
            cv2.circle(image, (x, y), 3, (0, 0, 255), -1)

# 빈 이미지 생성
image = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Draw Polygon')
cv2.setMouseCallback('Draw Polygon', draw_polygon)

# 변수 초기화
drawing = False  # 다각형 그리기 상태
points = []  # 다각형 점 좌표

# 메인 루프
while True:
    cv2.imshow('Draw Polygon', image)
    key = cv2.waitKey(1) & 0xFF

    # 'r' 키를 누르면 이미지 초기화
    if key == ord('r'):
        image = np.zeros((512, 512, 3), np.uint8)
        drawing = False
        points = []

    # 'q' 키를 누르면 종료
    if key == ord('q'):
        break

cv2.destroyAllWindows()