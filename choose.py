import cv2
import numpy as np

# Ask user for the primary color
color = input("Enter a primary color to track (red, green, blue): ").lower()

# Define HSV ranges for common primary colors
hsv_ranges = {
    'red': [((0, 100, 100), (10, 255, 255)), ((160, 100, 100), (180, 255, 255))],  # Two ranges for red
    'green': [((35, 100, 100), (85, 255, 255))],
    'blue': [((100, 100, 100), (130, 255, 255))]
}

if color not in hsv_ranges:
    print("Invalid color! Choose from red, green, blue.")
    exit()

# Start capturing video
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Apply the mask(s) for selected color
    mask = None
    for lower, upper in hsv_ranges[color]:
        lower_np = np.array(lower)
        upper_np = np.array(upper)
        current_mask = cv2.inRange(hsv, lower_np, upper_np)
        if mask is None:
            mask = current_mask
        else:
            mask = cv2.bitwise_or(mask, current_mask)

    # Extract result using the mask
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display results
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Tracked Color', result)

    if cv2.waitKey(1) & 0xff == 27:  # ESC to exit
        break

capture.release()
cv2.destroyAllWindows()
