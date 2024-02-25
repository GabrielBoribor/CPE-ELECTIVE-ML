import cv2 as cv
from matplotlib import pyplot as plt

# Read the image
img = cv.imread("HOI.jpg")
img_color = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # Convert BGR to RGB for displaying with Matplotlib

# Apply Sobel edge detection
sobelx = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)  # Sobel filter in X direction(pahiga)
sobely = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)  # Sobel filter in Y direction(patayo)
sobelxy = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)  # Sobel filter in both X and Y directions

# Convert the output back to uint8
filtered_image_x = cv.convertScaleAbs(sobelx)
filtered_image_y = cv.convertScaleAbs(sobely)
filtered_image_xy = cv.convertScaleAbs(sobelxy)

# Plot the images
plt.figure(figsize=(20, 20))

plt.subplot(221)
plt.imshow(img_color, cmap='gray')  # Display the original image
plt.title('Original')
plt.axis("off")  # Hide axis

plt.subplot(222)
plt.imshow(filtered_image_x, cmap='gray')  # Display the Sobel filtered image in X direction
plt.title('Sobel X')
plt.axis("off")  # Hide axis

plt.subplot(223)
plt.imshow(filtered_image_y, cmap='gray')  # Display the Sobel filtered image in Y direction
plt.title('Sobel Y')
plt.axis("off")  # Hide axis

plt.subplot(224)
plt.imshow(filtered_image_xy, cmap='gray')  # Display the Sobel filtered image in both X and Y directions
plt.title('Sobel XY')
plt.axis("off")  # Hide axis

plt.show()  # Show the plot with all images
