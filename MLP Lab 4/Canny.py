import cv2 as cv
from matplotlib import pyplot as plt

# Read the image
img = cv.imread("HOI.jpg")
img_color = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # Convert BGR to RGB for displaying with Matplotlib

# Apply Canny edge detection
edges = cv.Canny(img_color, 100, 200)  # Apply Canny edge detection with thresholds 100 and 200

# Plot the images
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.imshow(img_color)  # Display the original image
plt.title('Original')
plt.axis("off")  # Hide axis

plt.subplot(122)
plt.imshow(edges, cmap='gray')  # Display the detected edges
plt.title('Canny Edges')
plt.axis("off")  # Hide axis

plt.show()  # Show the plot with both images
