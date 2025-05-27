# Smart Dog Detector using YOLOv8
from ultralytics import YOLO
import cv2
import time
import os
import simpleaudio as sa

base_path = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(base_path, "alert.wav")

CONFIDENCE_THRESHOLD = 0.5

def run_detection():
    # Load YOLOv8 model
    model = YOLO("yolov8s.pt")
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Running YOLO Detection. Press 's' to take a snapshot, 'q' to stop.")

    last_detection_time = 0
    cooldown = 5  # seconds between alerts
    audio_playback = None  # to track the WaveObject Playback
    show_alert = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading from camera.")
            break

        # Run YOLO inference
        results = model(frame, imgsz=640)
        annotated_frame = results[0].plot()

        current_time = time.time()
        names = results[0].names
        dog_detected = False

        # Check each detection for "dog"
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = names[cls_id]

            if label == "dog" and conf > CONFIDENCE_THRESHOLD:
                dog_detected = True
                # Only trigger once per cooldown period
                if (current_time - last_detection_time) > cooldown:
                    last_detection_time = current_time
                    print(f"🐶 Dog detected with confidence {conf:.2f}")
                    timestamp = time.strftime("%Y%m%d-%H%M%S")
                    filename = f"snapshot_{timestamp}.jpg"
                    cv2.imwrite(filename, frame)
                    print(f"Snapshot saved as {filename}")

                    # Play alert if not already playing
                    if audio_playback is None or not audio_playback.is_playing():
                        try:
                            wave_obj = sa.WaveObject.from_wave_file(sound_path)
                            audio_playback = wave_obj.play()
                        except Exception as e:
                            print(f"Error playing sound: {e}")

                    show_alert = True
                break  # only handle one dog per frame

        # If the dog has gone, stop the sound & hide the text
        if not dog_detected and audio_playback and audio_playback.is_playing():
            audio_playback.stop()
            show_alert = False

        # Overlay warning text if needed
        if show_alert:
            cv2.putText(
                annotated_frame,
                "⚠️ Dog Detected!",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )

        # Show the frame
        cv2.imshow("YOLO Detection", annotated_frame)
        key = cv2.waitKey(1) & 0xFF

        # Manual snapshot
        if key == ord('s'):
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"snapshot_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Snapshot saved as {filename}")

        # Quit detection
        elif key == ord('q'):
            print("Exiting detection.")
            break

        # If window closed manually
        if cv2.getWindowProperty("YOLO Detection", cv2.WND_PROP_VISIBLE) < 1:
            print("Window closed.")
            break

    # Ensure sound is stopped on exit
    if audio_playback and audio_playback.is_playing():
        audio_playback.stop()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    while True:
        print("\n📷 Smart Dog Detector Menu")
        print("Press 'r' to run YOLO detection")
        print("Press 'q' to quit the program")
        choice = input("Your choice: ").strip().lower()

        if choice == 'r':
            run_detection()
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please press 'r' or 'q'.")
