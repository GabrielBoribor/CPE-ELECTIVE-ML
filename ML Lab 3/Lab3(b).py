import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('CJ.png')
GBlur = cv.GaussianBlur(img,(55,5),0)



plt.subplot(121), plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(GBlur),plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([])
plt.show()