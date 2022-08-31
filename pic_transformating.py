import cv2
import numpy as np

img = cv2.imread('images/b1.jpg')

# flipping
new_img = cv2.flip(img, -1)


# rotating
def rotate(img, angle):
    height, width = img.shape[:2]
    point = (width // 2, height // 2)

    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img, mat, (width, height))


new_img1 = rotate(img, 90)


# transforming
def transform(img, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img, mat, (img.shape[1], img.shape[0]))


new_img2 = transform(img, 100, 100)

# contour search
new_img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
new_img3 = cv2.GaussianBlur(new_img3, (5, 5), 0)

new_img3 = cv2.Canny(img, 100, 140)

con, hir = cv2.findContours(new_img3, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# creating pic from contours
new_img4 = np.zeros(img.shape, np.uint8)
cv2.drawContours(new_img4, con, -1, (230, 111, 236), 5)

cv2.imshow('Result', new_img4)
cv2.waitKey(0)
