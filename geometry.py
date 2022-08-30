import cv2
import numpy as np


# black image
img = np.zeros((450, 450, 3), np.uint8)

# black img to red
img[:] = 66, 72, 245

# green square on img
img[100:150, 200:280] = 119, 201, 105

# rectangle
cv2.rectangle(img, (0, 0), (100, 100), (119, 201, 105), 3)

# line
cv2.line(img, (450, 0), (50, 0), (119, 201, 105), 10)

# circle in the middle
cv2.circle(img, (img.shape[1] // 2, img.shape[0]//2), 50, (119, 201, 105), 5)

# text
cv2.putText(img, 'OpenCV', (250, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 0), 3)


cv2.imshow('Result', img)
cv2.waitKey(0)