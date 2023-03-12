import cv2

# Define the function that will be called when a mouse event occurs
def on_mouse(event, x, y, flags, param):
    global roi, roi_selected, roi_window

    # If the left mouse button is down, capture the position and draw a rectangle
    if event == cv2.EVENT_LBUTTONDOWN:
        roi = (x, y)
        roi_selected = False
    elif event == cv2.EVENT_LBUTTONUP:
        roi_selected = True
        cv2.rectangle(frame, roi, (x, y), (0, 255, 0), 2)

        # Create a new window to display the ROI and show the ROI in the new window
        roi_window = cv2.namedWindow('ROI')
        roi_frame = frame[roi[1]:y, roi[0]:x]
        cv2.imshow('ROI', roi_frame)

    # If the right mouse button is up, delete the rectangle and close the ROI window
    elif event == cv2.EVENT_RBUTTONUP:
        cv2.rectangle(frame, roi, (x, y), (0, 0, 0), 2)
        roi_selected = False
        cv2.destroyWindow('ROI')

# Create a window to display the output video frame
cv2.namedWindow('output')

# Set up the mouse callback function for the output window
cv2.setMouseCallback('output', on_mouse)

# Define the text to be displayed on the video frame
text = "              MBS3523 Assignment 1 Q6    Name: Sin Ka Hin Oscar"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 2
text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
text_x = int((640 - text_size[0]) / 2)
text_y = int(text_size[1] * 2)

# Initialize the ROI variables
roi = (0, 0)
roi_selected = False
roi_window = None

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

    # If an ROI has been selected, display the selected ROI
    if roi_selected:
        roi_frame = frame[roi[1]:, roi[0]:]
        cv2.imshow('ROI', roi_frame)

    # Add the text label to the top middle of the video frame
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, (255, 255, 255), thickness)

    # Display the output frame
    cv2.imshow('output', frame)

    # Wait for a key press and check if the user wants to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
