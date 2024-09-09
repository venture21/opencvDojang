import cv2
import matplotlib.pyplot as plt

def hist_gray(src):
    # src의 히스토그램을 가져오기
    hist = cv2.calcHist([src], [0], None, [256], [0,256])
    plt.plot(hist)
    plt.show()