import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

# Store all drawing points
points = []

while True:

    # Read frame
    success, frame = cap.read()

    if not success:
        print("Error: Cannot read frame")
        break

    # Flip the image so movement feels natural
    frame = cv2.flip(frame, 1)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ==========================
    # Choose the marker color
    # (Example: Blue)
    # ==========================

    lower = np.array([100, 150, 50])
    upper = np.array([140, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower, upper)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the biggest contour
    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 500:

            x, y, w, h = cv2.boundingRect(contour)

            # Tip of the marker
            cx = x + w // 2
            cy = y

            # Save point
            points.append((cx, cy))

            # Show marker position
            cv2.circle(frame, (cx, cy), 10, (0, 0, 255), cv2.FILLED)

    # Draw all saved points
    for point in points:
        cv2.circle(frame, point, 8, (255, 0, 0), cv2.FILLED)

    cv2.imshow("Virtual Paint", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)

    # Press q to quit
    if key == ord("q"):
        break

    # Press c to clear drawing
    if key == ord("c"):
        points.clear()

cap.release()
cv2.destroyAllWindows()