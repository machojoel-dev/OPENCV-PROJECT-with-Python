import cv2  

# Open the default webcam (camera index 0)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()  # Stop the program if the camera cannot be opened

# Continuously capture and display video frames
while True:

    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Cannot read frame")
        break  # Exit the loop if a frame cannot be read

    # Display the captured frame in a window named "video"
    cv2.imshow("video", frame)

    # Wait for 1 millisecond for a key press
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera so other applications can use it
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()