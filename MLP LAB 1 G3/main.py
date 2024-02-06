# Python code to read image
import cv2
img = cv2.imread("LBJ.jpg", cv2.IMREAD_COLOR)

# Creating GUI window to display an image screen
cv2.imshow("LBJ", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

