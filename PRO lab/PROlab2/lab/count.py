
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('e1.jpg')
plt.imshow(img, cmap='gray'),plt.title('ORIGINAL')
plt.show()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray'),plt.title('ORIGINAL')
plt.show()

blur = cv2.GaussianBlur(gray, (11,11),0)
plt.imshow(blur, cmap='gray')
plt.show()

canny = cv2.Canny(blur, 1,69, 1)
plt.imshow(canny, cmap='gray')
plt.show()

dilated = cv2.dilate(canny, (1,10), iterations = 2)
plt.imshow(dilated, cmap='gray')
plt.show()

(cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
contorno = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.drawContours(contorno,cnt, -1,(1,300,1),2)
plt.imshow(contorno),plt.title('Zliczone komórki')
plt.show()
print(f'Komórki zliczone podczas analizy obrazu: {len(cnt)}')