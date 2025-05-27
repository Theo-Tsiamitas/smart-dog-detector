# yolo_loop.py
# Smart Dog Detector using YOLOv8
import os
import time
import cv2
import simpleaudio as sa
from ultralytics import YOLO
 
base_path = os.path.dirname(__file__)
snapshot_dir = os.path.join(base_path, "snapshots")   # A folder named snapshots will be created
os.makedirs(snapshot_dir, exist_ok=True)   # All snapshots can be saved inside it automatically.

sound_path = os.path.join(base_path, "alert.wav")
CONFIDENCE_THRESHOLD = 0.5

def run_detection():
    model = YOLO("yolov8s.pt")
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Running YOLO Detection. Press 's' to take a snapshot, 'q' to stop.")

    last_detection_time = 0
    cooldown = 5  # seconds between *new* snapshots
    alert_played = False
    audio_playback = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading from camera.")
            break

        results = model(frame, imgsz=640)
        annotated = results[0].plot()
        now = time.time()

        # once we've played, we never play again this run
        if not alert_played:
            for box in results[0].boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                if results[0].names[cls_id]=="dog" and conf>CONFIDENCE_THRESHOLD:
                    # first time dog seen
                    print(f"🐶 Dog detected ({conf:.2f})")
                    filename = f"snapshot_{time.strftime('%Y%m%d-%H%M%S')}.jpg"
                    filepath = os.path.join(snapshot_dir, filename)
                    cv2.imwrite(filepath, frame)
                    print(f"Snapshot saved as {filepath}")
                    try:
                        wave_obj = sa.WaveObject.from_wave_file(sound_path)
                        audio_playback = wave_obj.play()
                    except Exception as e:
                        print("Error playing sound:", e)
                    alert_played = True
                    break

        # if alert_played, overlay text forever
        if alert_played:
            cv2.putText(
                annotated, "⚠️ Dog Detected!", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3
            )

        cv2.imshow("YOLO Detection", annotated)
        key = cv2.waitKey(1) & 0xFF

        if key==ord('s'):
            ts = time.strftime("%Y%m%d-%H%M%S")
            fn = f"snapshot_{ts}.jpg"
            cv2.imwrite(fn, frame)
            print(f"Snapshot saved as {fn}")
        elif key==ord('q'):
            print("Exiting detection.")
            break

        # if user closes window with the X
        if cv2.getWindowProperty("YOLO Detection", cv2.WND_PROP_VISIBLE)<1:
            print("Window closed.")
            break

    # stop the sound on exit
    if audio_playback and audio_playback.is_playing():
        audio_playback.stop()

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    while True:
        print("\n📷 Smart Dog Detector Menu")
        print(" Press 'r' to run YOLO detection")
        print(" Press 'q' to quit")
        choice = input("Your choice: ").strip().lower()
        if choice=='r':
            run_detection()
        elif choice=='q':
            print("Goodbye!")
            break
        else:
            print("Invalid input—please press 'r' or 'q'.")
