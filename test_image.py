
import cv2

print("Package imported successfully")

img = cv2.imread("images/sunset.jpg")

cv2.imshow("output", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
