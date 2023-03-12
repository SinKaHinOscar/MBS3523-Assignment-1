import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Create two windows, one for color image and one for grayscale image
cv2.namedWindow("Color Frame", cv2.WINDOW_NORMAL)
cv2.namedWindow("Grayscale Frame", cv2.WINDOW_NORMAL)

while True:
    # Read the image captured by the webcam
    ret, frame = cap.read()

    # If cannot read the image, exit the program
    if not ret:
        print("Cannot receive frame (stream end?). Exiting ...")
        break

    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the color and grayscale images in their respective windows
    cv2.imshow("Color Frame", frame)
    cv2.imshow("Grayscale Frame", gray)

    # Press 'q' to exit the program
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam resources
cap.release()

# Close all windows
cv2.destroyAllWindows()

