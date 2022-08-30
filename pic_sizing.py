import cv2
import numpy as np


img = cv2.imread('images/b1.jpg')
print(img.shape)

# resize
new_img1 = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

# cutting
new_img2 = img[0:100, 0:150]

# blurring (only odd values in tuple)
new_img3 = cv2.GaussianBlur(img, (59, 59), 10)

# change color format
new_img4 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# edge detection
new_img5 = cv2.Canny(img, 100, 100)

# dilation and erosion
kernel = np.ones((5, 5), np.uint8)
new_img6 = cv2.dilate(img, kernel, iterations=1)
new_img7 = cv2.erode(img, kernel, iterations=10)


cv2.imshow('Result', new_img7)
cv2.waitKey(0)

