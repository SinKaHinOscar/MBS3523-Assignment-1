import cv2
import numpy as np

# Open the video capture device (webcam)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error opening video capture device")
    exit()

# Define the text to be displayed on the video frame
text = "MBS3523 Assignment 1 Q4    Name: Sin Ka Hin Oscar"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 2
text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
text_x = int((cap.get(cv2.CAP_PROP_FRAME_WIDTH) - text_size[0]) / 2)
text_y = int(text_size[1] * 2)

while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()
    if not ret:
        print("Error reading video frame")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Loop over each detected face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Convert the rectangle mask to uint8 data type
        mask = cv2.rectangle(frame.copy(), (x, y), (x+w, y+h), (255, 255, 255), -1).astype('uint8')

        # Apply the binary mask to the color frame outside the rectangle
        color_outside = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))

        # Combine the color frame inside the rectangle and the color frame outside the rectangle
        output = cv2.add(gray_outside, color_outside)

        # Add the text label to the top middle of the video frame
        cv2.putText(output, text, (text_x, text_y), font, font_scale, (255, 255, 255), thickness)

        # Display the output frame
        cv2.imshow('output', output)

    # Wait for a key press and check if the user wants to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
