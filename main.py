import cv2
import numpy as np
import pytesseract
# 입력 이미지
img = cv2.imread("test.jpg")
# 입력받은 이미지에 대해 인식율을 높이기 위해 이미지 확대 및 3차보간
img = cv2.resize(img, (800,640), cv2.INTER_CUBIC)
# 노이즈 줄이기
img = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=0.5)
# 이미지 이진화
binary_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 윤곽선 검출
canny = cv2.Canny(binary_img, 100, 250)
# closing 연산으로 윤곽선 사이의 빈 영역을 채운다.
kernel = np.ones((3,3), np.uint8)
result = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
dilate_result = cv2.dilate(result, kernel, iterations=1)
# 테서랙트 OCR로 검출
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\LUA\\Documents\\Tesseract-OCR\\tesseract.exe'
chars = pytesseract.image_to_string(dilate_result, lang='kor')
print(chars)
cv2.imshow('test', result)
cv2.imshow('compare', dilate_result)
cv2.waitKey()
