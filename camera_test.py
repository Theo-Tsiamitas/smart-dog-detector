import cv2
import simpleaudio as sa
import time
last_alert_time = 0


# Load the reference image and convert it to grayscale
reference = cv2.imread('reference.jpg')
reference_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
reference_gray = cv2.GaussianBlur(reference_gray, (21, 21), 0)

# Open the default camera (usually webcam)
cap = cv2.VideoCapture(1)

alert_triggered = False

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
else:
    print("Camera opened successfully! Press 'Space' to capture a photo or 'q' to quit.")

    

# Keep the camera window open
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    # Convert current frame to grayscale and blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Compute difference between current frame and reference
    diff = cv2.absdiff(reference_gray, gray)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # Count the number of changed pixels
    change = cv2.countNonZero(thresh)

    # Show the threshold difference
    cv2.imshow('Difference', thresh)

    # If change is significant, show alert
    if change > 5000:
        cv2.putText(frame, "⚠️ Movement Detected!", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        print("Change detected!")

        # Play sound only if 5 seconds have passed since last one
        if time.time() - last_alert_time > 5:
            wave_obj = sa.WaveObject.from_wave_file('alert.wav')
            play_obj = wave_obj.play()  # play without waiting
            last_alert_time = time.time()  # update alert time
        else:
            alert_triggered = False  # optional: reset flag

    # Show the live feed
    cv2.imshow('Live Feed', frame)

    # Check if user pressed a key
    key = cv2.waitKey(1) & 0xFF

    # ALSO: Check if window was manually closed (extra safety)
    if cv2.getWindowProperty('Live Feed', cv2.WND_PROP_VISIBLE) < 1:
        print("Window was closed.")
        break

    if key == ord(' '):  # Save a snapshot
        cv2.imwrite('captured.jpg', frame)
        print("Snapshot saved as captured.jpg")

    elif key == ord('q'):  # Quit properly
        print("Quitting...")
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()