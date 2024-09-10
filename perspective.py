import cv2, sys
import numpy as np


radius = 25

# 직선과 원을 그리는 함수
def drawROI(img, corners):
    global radius
    cpy = img.copy()
    
    # 컬러 지정
    c1 = (192,192,255) #원의 색상
    c2 = (128,128,255) #직선의 색상
    
    lineWidth = 2
    
    #원을 그린다.(4개 좌표점이 있다.)
    for pt in corners:     
        cv2.circle(cpy, tuple(pt.astype(int)), radius, c1, -1,cv2.LINE_AA)

    # 4개 모서리 라인 그리기
    cv2.line(cpy, tuple(corners[0].astype(int)),tuple(corners[1].astype(int)),c2, lineWidth, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[1].astype(int)),tuple(corners[2].astype(int)),c2, lineWidth, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[2].astype(int)),tuple(corners[3].astype(int)),c2, lineWidth, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[3].astype(int)),tuple(corners[0].astype(int)),c2, lineWidth, cv2.LINE_AA)
    
    # alpha=0.3, beta=0.7, gamma=0
    disp = cv2.addWeighted(img,0.3,cpy,0.7,0)

    return disp


#마우스 좌표를 얻기 위해 콜백함수 사용
def mouse_callback(event, x, y, flags, param):
    global srcQuad, dragSrc, img2, radius, ptOld
    
    # 왼쪽 버튼을 누르고 있을때
    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            # 현재 마우스 위치가 4개 모서리 포인트중 원안에 들어가는가?
            if cv2.norm(srcQuad[i]-(x,y))<radius:
                dragSrc[i] = True
                # 마우스로 이동하기 전의 위치
                ptOld = (x,y)
                # 만약에 현재 이동할 모서리를 확인하면 for문을 빠져 나옴
                break
    
    if event==cv2.EVENT_LBUTTONUP:
        for i in range(4):
            # dragSrc는 현재 이동중이 모서리 포인트를 True
            dragSrc[i] = False
    
    # 모서리 원과 직선을 새로 그려서 업데이트
    if event==cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]:
                dx = x - ptOld[0] #ptOld(x,y)
                dy = y - ptOld[1]
                
                srcQuad[i] += (dx,dy)
                # 창에 업데이트
                cpy = drawROI(img2, srcQuad)
                cv2.imshow('img',cpy)
                ptOld = (x,y)
                break
  


img = cv2.imread('data2/book.jpg')

if img is None:
    sys.exit('Image load failed')
    
img2 = cv2.resize(img,(0,0),None,fx=0.5,fy=0.5)

w, h = img2.shape[1], img2.shape[0] 
print(w,h)

# 다각형의 좌표를 그릴때는 시계방향으로()
spare = 50
srcQuad = np.array([[spare,spare],[w-spare,spare],[w-spare,h-spare],[spare,h-spare]], np.float32)

# 변환될 좌표
dstQuad = np.array([[0,0],[w-1,0],[w-1,h-1],[0, h-1]],np.float32)
# 마우스 포인터로 4개 좌표를 이동했는지 체크하는 플래그
dragSrc = [False,False,False,False]

#처음 한번은 직접 화면에 drawROI함수를 호출해서 그려준다.
disp = drawROI(img2,srcQuad)

cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_callback,[img2])
cv2.imshow('img',disp)
#cv2.imshow('dst',dst)

while True:
    #키입력 'Enter'->이미지 변환, 'ESC'-> 종료 키 입력
    key = cv2.waitKey()
    if key == 13: # Enter ASCII테이블 참조
        break
    elif key==27: # ESC
        cv2.destroyAllWindows()
        sys.exit()



# 변환 행렬 생성
# srcQuad는 mouse_callback함수에서 update
pers = cv2.getPerspectiveTransform(srcQuad,dstQuad)
dst = cv2.warpPerspective(img2,pers,(w,h))

cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()
