from ultralytics import YOLO
import cv2

# Load a pre-trained YOLOv8 model (YOLOv8n = nano = very fast)
model = YOLO("yolov8n.pt")  # Downloads automatically if not found

# Start webcam
cap = cv2.VideoCapture(1)  # Change to 1 if needed

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection on the frame
    results = model(frame, imgsz=640)

    # Plot results on the frame
    annotated_frame = results[0].plot()

    # Show the frame
    cv2.imshow("YOLO Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
