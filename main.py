import cv2

# Task 1: Initialize the laptop camera using OpenCV
camera = cv2.VideoCapture(0)

# Task 2: Load the pre-trained human detection model
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    # Task 3: Read frames from the camera and convert to grayscale
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Task 3: Apply human detection model
    boxes, scores = hog.detectMultiScale(gray, winStride=(4, 4), padding=(8, 8), scale=1.05)

    # Task 4: Draw rectangles around detected humans on the original frame
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Task 5: Calculate the total number of humans detected
    total_humans = len(boxes)

    # Task 4: Display the frame with bounding boxes
    cv2.imshow('Human Detection', frame)

    # Task 5: Print the count of detected humans
    print("Total Humans Detected:", total_humans)

    # Task 6: Break condition to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Task 6: Release the camera
camera.release()
cv2.destroyAllWindows()
