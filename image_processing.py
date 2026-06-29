# Basic image processing using OpenCV: grayscale, Gaussian blur, edge detection, dilation, and erosion.

# Basic image processing using OpenCV.
import cv2
import numpy as np

# Load the image
image = cv2.imread("images/girl2.jpg")

# Create a 5x5 kernel for image processing
kernel = np.ones((5, 5), np.uint8)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur the grayscale image
blurred_image = cv2.GaussianBlur(gray_image, (7, 7), 0)

# Detect edges
edges = cv2.Canny(gray_image, 150, 200)

# Make the edges thicker
dilated_image = cv2.dilate(edges, kernel, iterations=1)

# Make the edges thinner again
eroded_image = cv2.erode(dilated_image, kernel, iterations=1)

# Show each result
cv2.imshow("Original", image)
#cv2.imshow("Grayscale", gray_image)
#cv2.imshow("Blurred", blurred_image)
cv2.imshow("Edges", edges)
#cv2.imshow("Dilated", dilated_image)
#cv2.imshow("Eroded", eroded_image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()