import cv2
import numpy as np

# Define the function that will be called when the trackbar is moved
def on_trackbar(pos):
    global x
    x = pos

# Create a window to display the output video frame
cv2.namedWindow('output')

# Create a trackbar to adjust the position of the vertical line
cv2.createTrackbar('Line Position', 'output', 0, 640, on_trackbar)

# Define the text to be displayed on the video frame
text = "             MBS3523 Assignment 1 Q5 Name: Sin Ka Hin Oscar"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 2
text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
text_x = int((640 - text_size[0]) / 2)
text_y = int(text_size[1] * 2)

# Initialize the position of the vertical line
x = 320

# Open the video capture device (webcam)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error opening video capture device")
    exit()

while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()
    if not ret:
        print("Error reading video frame")
        break

    # Draw the vertical line on the frame
    cv2.line(frame, (x, 0), (x, 480), (0, 255, 0), 2)

    # Add the text label to the top middle of the video frame
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, (255, 255, 255), thickness)

    # Display the output frame
    cv2.imshow('output', frame)

    # Wait for a key press and check if the user wants to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Get the position of the trackbar and update the position of the vertical line
    pos = cv2.getTrackbarPos('Line Position', 'output')
    x = pos

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
