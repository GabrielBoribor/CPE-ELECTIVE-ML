import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

def apply_filters(frame):
    # Resize the frame to a smaller size
    small_frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # Sobel XY
    sobelxy = cv.Sobel(small_frame, cv.CV_64F, dx=1, dy=1, ksize=5)
    filtered_sobelxy = cv.convertScaleAbs(sobelxy)
    # Canny Edge
    canny = cv.Canny(small_frame, 50, 150)
    # Laplacian Edge
    laplacian_edges = cv.Laplacian(small_frame, cv.CV_64F)
    laplacian_edges = cv.convertScaleAbs(laplacian_edges)

    return small_frame, filtered_sobelxy, canny, laplacian_edges

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Function to update the Matplotlib plot with new frames
def update_plot(frame):
    small_frame, filtered_sobelxy, canny, laplacian_edges = apply_filters(frame)

    # Display the frames with appropriate labels
    axes[0, 0].imshow(cv.cvtColor(small_frame, cv.COLOR_BGR2RGB))
    axes[0, 0].set_title('Original')

    axes[0, 1].imshow(filtered_sobelxy, cmap='gray')
    axes[0, 1].set_title('Sobel XY')

    axes[1, 0].imshow(canny, cmap='gray')
    axes[1, 0].set_title('Canny Edges')

    axes[1, 1].imshow(laplacian_edges, cmap='gray')
    axes[1, 1].set_title('Laplacian Edges')

    plt.pause(0.01)  # Pause to update the plot

# Set frames per second (fps) and calculate interval
fps = 30
interval = int(1000 / fps)

# Read and process each frame from the camera
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    update_plot(frame)

    # Check for key press to exit the loop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object, close the Matplotlib window, and release the camera
cap.release()
plt.close()
cv.destroyAllWindows()
