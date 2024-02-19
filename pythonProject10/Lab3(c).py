import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Halata.png')
Median = cv.medianBlur(img,5)



plt.subplot(121), plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(Median),plt.title('Median Blur')
plt.xticks([]), plt.yticks([])
plt.show()