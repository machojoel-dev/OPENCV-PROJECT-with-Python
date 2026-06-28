import cv2

# Load the image
img = cv2.imread("images/woman.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the grayscale image
blur = cv2.GaussianBlur(gray, (7, 7), 0)

# Display the images
cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Blurred", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()