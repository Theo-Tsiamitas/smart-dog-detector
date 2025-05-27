# 🐶 Smart Dog Couch Detector

A real-time, AI-powered dog detection system that watches your couch when you can't. Built with [YOLOv8](https://github.com/ultralytics/ultralytics), OpenCV, and Python, this project alerts you when your dog gets where they shouldn't — by taking photos, playing sounds, and displaying visual warnings on screen.

---

## 🔍 What It Does

- 🐕 Detects dogs using the webcam in real time  
- 🔔 Plays a warning sound when a dog is detected  
- 📸 Saves a snapshot automatically when detection occurs  
- 🖼️ Displays an on-screen "Dog Detected!" warning  
- 🧠 Filters false positives with confidence thresholds  
- 🎛️ Lets you manually take photos, restart detection, or quit the program  
- 📁 Organizes all snapshots into a dedicated folder  

---

## 📸 Demo

> (Optional: Add a screenshot or short GIF here of the detection in action - Coming soon)

---

## 🧪 How to Use

### 1. Clone or download this repository

```bash
git clone https://github.com/Theo-Tsiamitas/smart-dog-detector.git
cd smart-dog-detector
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the program

```bash
python yolo_loop.py
```

### 4. Use the menu

| Key | Function                       |
|-----|--------------------------------|
| `r` | Run detection                  |
| `s` | Save a manual snapshot         |
| `q` | Quit detection or exit program |

Snapshots are saved automatically inside the `snapshots/` folder.

---

## 📁 Project Structure

```
smart-dog-detector/
├── yolo_loop.py           # Main script
├── alert.wav              # Custom or default alert sound
├── snapshots/             # All captured images go here
├── requirements.txt       # Required Python packages
├── .gitignore             # Files to ignore in Git
└── README.md              # You're reading this
```

---

## ⚙️ Requirements

- Python 3.10 or higher
- Webcam
- `ultralytics`, `opencv-python`, `simpleaudio`

Install them via:

```bash
pip install -r requirements.txt
```

---

## 💡 Ideas for Expansion

- Train the model to recognize your dog specifically  
- Add cloud syncing or Telegram alerts  
- Convert to a mobile or Raspberry Pi version  
- Track and log dog behavior over time  

---

## 🙋 Developer Note

This project was built and tested by me, **Theodoros Tsiamitas**, as part of my early hands-on journey into AI-powered automation. I used Python and the Ultralytics YOLOv8 model to turn a real-life problem into a working detection system — guided by my design decisions, logic, and practical experimentation.

I'm a self-driven learner exploring AI and full-stack development by solving real-life problems in creative ways. I'm continuously improving this project as part of my long-term goal to become a professional full-stack developer.

💬 Want to collaborate, give feedback, or help turn this into a real product? Feel free to reach out!

---

## 📜 License

This project is open for educational and personal use. Please contact the author for commercial licensing or collaboration.

---

## 👤 Created by

**Theodoros Tsiamitas**  
AI-Driven Problem Solver | Future Full-Stack Developer  
[GitHub](https://https://github.com/Theo-Tsiamitas) | [LinkedIn](https://www.linkedin.com/in/theodoros-tsiamitas-a706b325a/)

