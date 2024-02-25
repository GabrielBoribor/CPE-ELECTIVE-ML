import cv2 as cv
from matplotlib import pyplot as plt

# Read the image
img = cv.imread("HOI.jpg")
img_color = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # Convert BGR to RGB for displaying with Matplotlib

# Apply Laplacian edge detection
laplacian = cv.Laplacian(img_color, cv.CV_64F)
filtered_image_x = cv.convertScaleAbs(laplacian)  # Convert the result to an unsigned 8-bit image

# Plot the images
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.imshow(img_color)  # Display the original image
plt.title('Original')
plt.axis("off")  # Hide axis

plt.subplot(122)
plt.imshow(filtered_image_x, cmap='gray')  # Display the Laplacian edges (converted to unsigned 8-bit)
plt.title('Laplacian Edges')
plt.axis("off")  # Hide axis

plt.show()  # Show the plot with both images
