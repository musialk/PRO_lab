import cv2

img = cv2.imread('stereoPara.jpg', cv2.IMREAD_UNCHANGED)

y=0
x=0
h=1080
w=958
crop_img = img[y:y+h, x:x+w]

cv2.imwrite('stereo1.jpg', crop_img)