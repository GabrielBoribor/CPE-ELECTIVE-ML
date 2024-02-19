import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Halata.png')
blur = cv.blur(img,(5,55))

plt.subplot(121), plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(blur),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()