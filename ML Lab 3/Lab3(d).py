import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Halata.png')
Bblur = cv.bilateralFilter(img,20,200,200)


plt.subplot(121), plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(Bblur),plt.title('Bilateral Filter')
plt.xticks([]), plt.yticks([])
plt.show()