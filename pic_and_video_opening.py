import cv2

# picture opening
img = cv2.imread('images/b1.jpg')
cv2.imshow('Result', img)
cv2.waitKey(0)

# video opening
cap = cv2.VideoCapture('videos/B2 Stealth Bomber arrival Fairford (FFD).mp4')
while True:
    success, img = cap.read()
    cv2.imshow('Result', img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# camera opening
cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 300)
while True:
    success, img = cap.read()
    cv2.imshow('Result', img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
