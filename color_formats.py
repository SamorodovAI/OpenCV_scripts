import cv2

img = cv2.imread('images/b1.jpg')

# from one format to another
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# stratification
r, g, b = cv2.split(img)

# layering
img = cv2.merge([b, g, r])


cv2.imshow('Result', img)
cv2.waitKey(0)
