import cv2

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open webcam.")
    exit()

while True:
    success, img = cap.read()

    if not success:
        print("Failed to grab frame.")
        break

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()