import cv2
import numpy as np

# Open the webcam
cap = cv2.VideoCapture(0)

# Set the frame size
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the box size and initial position
box_size = 80
box_x = np.random.randint(0, frame_width - box_size)
box_y = np.random.randint(0, frame_height - box_size)

# Define the box velocity and angle
box_speed = 10
box_angle = np.random.randint(15, 75)

# Define the text to display at the top of the frame
text = "MBS3523 Assignment 1  Q3    Name: Sin Ka Hin Oscar"

# Define the font properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2

while True:
    # Read the image captured by the webcam
    ret, frame = cap.read()

    # If cannot read the image, exit the program
    if not ret:
        print("Cannot receive frame (stream end?). Exiting ...")
        break

    # Draw the box on the frame
    cv2.rectangle(frame, (box_x, box_y), (box_x + box_size, box_y + box_size), (0, 255, 0), -1)

    # Draw the text at the top of the frame
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_x = int((frame_width - text_size[0]) / 2)
    cv2.putText(frame, text, (text_x, 50), font, font_scale, (0, 0, 255), font_thickness)

    # Update the box position based on the velocity and angle
    box_x += int(box_speed * np.cos(np.deg2rad(box_angle)))
    box_y += int(box_speed * np.sin(np.deg2rad(box_angle)))

    # Check if the box is out of bounds
    if box_x < 0:
        box_x = 0
        box_angle = 180 - box_angle
    elif box_x + box_size > frame_width:
        box_x = frame_width - box_size
        box_angle = 180 - box_angle

    if box_y < 0:
        box_y = 0
        box_angle = -box_angle
    elif box_y + box_size > frame_height:
        box_y = frame_height - box_size
        box_angle = -box_angle

    # Display the frame
    cv2.imshow("Bouncing Box", frame)

    # Press 'q' to exit the program
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam resources
cap.release()

# Close all windows
cv2.destroyAllWindows()
