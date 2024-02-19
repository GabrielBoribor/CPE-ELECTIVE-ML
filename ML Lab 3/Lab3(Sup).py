import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Halata.png')
blur = cv.blur(img,(5,55))
Gblur = cv.GaussianBlur(img,(55,5),0)
Median = cv.medianBlur(img,5) # Applying MedianBlur
Bblur = cv.bilateralFilter(img,20,200,200)

font= cv.FONT_HERSHEY_SIMPLEX




cv.putText(blur,'Averaging',(30,30), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
cv.putText(Gblur,'Gaussian Blur',(1,30), font, 1, (0,0,0), 2)
cv.putText(img,'Original',(30,30), font, 1, (0,0,0), 2)
cv.putText(Median,'Median',(30,30), font, 1, (0,0,0), 2)
cv.putText(Bblur,'Bilateral Filtering',(30,30), font, 1, (0,0,0), 2)

plt.subplot(331), plt.imshow(blur)
plt.xticks([]), plt.yticks([])

plt.subplot(333), plt.imshow(Gblur)
plt.xticks([]), plt.yticks([])

plt.subplot(335), plt.imshow(img)
plt.xticks([]), plt.yticks([])

plt.subplot(337), plt.imshow(Median)
plt.xticks([]), plt.yticks([])

plt.subplot(339), plt.imshow(Bblur)
plt.xticks([]), plt.yticks([])
plt.show()
