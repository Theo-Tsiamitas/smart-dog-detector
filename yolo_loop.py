# This is a test change in the test-detection-fix branch

from ultralytics import YOLO
import cv2
import time
import os

def run_detection():
    # Load YOLOv8 nano model
    model = YOLO("yolov8s.pt")

    # Open the webcam (change to 1 if needed)
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Running YOLO Detection. Press 's' to take a snapshot, 'q' to stop.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading from camera.")
            break

        # Run YOLO detection
        results = model(frame, imgsz=640)
        annotated_frame = results[0].plot()

        # Show live detection
        cv2.imshow("YOLO Detection", annotated_frame)

        # Handle keypresses
        key = cv2.waitKey(1) & 0xFF

        # Take a snapshot
        if key == ord('s'):
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"snapshot_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Snapshot saved as {filename}")

        # Quit detection
        elif key == ord('q'):
            print("Exiting detection.")
            break

        # Handle window closed manually
        if cv2.getWindowProperty("YOLO Detection", cv2.WND_PROP_VISIBLE) < 1:
            print("Window closed.")
            break

    cap.release()
    cv2.destroyAllWindows()


# Main program loop
while True:
    print("\n📷 Smart Dog Detector Menu")
    print("Press 'r' to run YOLO detection")
    print("Press 's' to capture a picture and save it")
    print("Press 'q' to quit the program")
    choice = input("Your choice: ").strip().lower()

    if choice == 'r':
        run_detection()
    elif choice == 'q':
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please press 'r' or 'q'.")
