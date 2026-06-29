import cv2
import numpy as np

path = "images/butterfly.jpg"
img = cv2.imread(path)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# HSV range for yellow
lower = np.array([20, 100, 100])
upper = np.array([35, 255, 255])

# Create a mask for yellow
mask = cv2.inRange(imgHSV, lower, upper)

# Show only the yellow parts
imgResult = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Original Image", img)
cv2.imshow("HSV Image", imgHSV)
#cv2.imshow("Mask", mask)
cv2.imshow("Yellow Detected", imgResult)

cv2.waitKey(0)
cv2.destroyAllWindows()
