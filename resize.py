import cv2

# Load the image
image = cv2.imread("images/girl.jpg")

# Display the original image size
print(image.shape)

# Resize the image (width, height)
resized_image = cv2.resize(image, (300, 200))
print(resized_image.shape)

# Crop the image: image[y1:y2, x1:x2]
cropped_image = image[100:400, 150:450]

# Display the images
cv2.imshow("Original", image)
cv2.imshow("Resized", resized_image)
cv2.imshow("Cropped", cropped_image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()