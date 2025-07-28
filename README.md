  
# 🏃‍♂️ Player Re-Identification in Sports Footage (Web App)

## 📌 Project Overview

This web application enables **automated player re-identification** in sports videos using computer vision. It supports:

- **Single-Camera Re-ID**: Track players in a single video feed(15sec_input_720p).
- **Cross-Camera Re-ID**: Match players across two video views (Broadcast, Tacticam) and generate a combined visual.

> Built using **Flask**, **YOLOv11**, **OpenCV**, and **feature-based matching**.

---

## 🚀 Features

✅ YOLOv11-based player detection  
✅ SORT algorithm for tracking  
✅ Feature-based ID matching using color histograms  
✅ Cross-view player association with identity lines  
✅ Web-based Flask UI for video upload & result visualization  
✅ Organized output video storage

---

## 🌐 Demo

🎥 **Demo Video**:  
https://github.com/user-attachments/assets/55c49b8a-7709-47a9-a22f-2c06d46212ea
---

## ✍️ Report
[Project Report.pdf](https://github.com/user-attachments/files/21221607/Project.Report.pdf)

---

## Outputs Vedios
### 🎥 Cross Camera Outputs Vedio
https://github.com/user-attachments/assets/fe8a11d6-5a2a-4c86-854d-d800dba1b5f6
---

### 🎥 Single Camera Outputs Vedio
https://github.com/user-attachments/assets/e4414599-2e5b-4c2f-a495-df505185b120
---

## 🖼️ Screenshots

### 🏠 Home Page  
> **Landing page of the system providing navigation to single or cross-camera modes.**
<img width="1366" height="768" alt="Screenshot (999)" src="https://github.com/user-attachments/assets/6b17f404-5d64-42a8-8ccf-0bb5ce210da1" />

### 📥 Upload Page (Single Camera)  
> **UI for uploading a single video(15sec_input_720p) for tracking players using YOLO and SORT.**
<img width="1366" height="768" alt="Screenshot (1008)" src="https://github.com/user-attachments/assets/04f39e8f-aed0-4f5d-9a36-262f833b2a74" />

### 📥 Upload Page (Cross Camera)  
> **Two video inputs (Broadcast, Tacticam) accepted to perform identity matching across multiple angles.**
<img width="1366" height="768" alt="Screenshot (1015)" src="https://github.com/user-attachments/assets/a9573f3b-4864-4b59-8a5e-18588b32ff68" />

### 🎞️ Input Video (Single Camera)  
> **Original video from a single feed () to be processed for player tracking.**
<img width="1366" height="563" alt="Front" src="https://github.com/user-attachments/assets/2d8b2fc8-1c5f-4fa2-be22-f41b1931a10c" />

### 🧵 Output Video (Single Camera)  
> **Resulting video image showing tracked players with persistent IDs within the same camera.**
<img width="1366" height="618" alt="Screenshot (1020)" src="https://github.com/user-attachments/assets/c1a5d516-9ac9-4cee-8a33-579d2b30d0e4" />

### 🎥 Input Videos (Cross Camera)  
> *two videos used for multi-camera player re-identification:*
> - **Broadcast Camera View**  
<img width="1366" height="748" alt="Screenshot (1016)" src="https://github.com/user-attachments/assets/6a50d448-334f-470f-8a00-0b7ebeeb942f" />

> - **Tacticam Camera View**  
<img width="1366" height="544" alt="Screenshot (1017)" src="https://github.com/user-attachments/assets/0df2a6cb-b950-4834-aafa-da836c20f27c" />

### 🎯 Output Video (Cross Camera Combined)  
> **Final combined video image with identity lines drawn to represent matched players across views.**
<img width="1366" height="605" alt="Screenshot (1018)" src="https://github.com/user-attachments/assets/5771672f-8f72-4eec-9271-9a3463fe08e7" />
---

## 🗂️ Folder Structure

```
Player Re-Identification Project/
├── app.py                     # 🎯 Main Flask backend app
├── requirements.txt           # 📦 Python dependencies
├── README.md                  # 📘 Project documentation

├── docs/                      # 📄 Project documentation & video
│   ├── Project Report         # Final Report (PDF)
│   └── Project Video          # Demo Video (MP4)

├── data/
│   └── uploads/               # 📤 Uploaded input videos
│       ├── 15sec_input_720p.mp4
│       ├── broadcast.mp4
│       └── tacticam.mp4

├── models/                    # 🤖 YOLOv11 model files
│   └── best.pt

├── static/
│   ├── outputs/
│   │   ├── reid_single/       # 🎯 Output videos for Single Camera mode
│   │   │   └── annotated_overview.mp4
│   │   └── reid_cross/        # 🔁 Combined output for Cross Camera mode
│   │       └── combined_video.mp4
│   ├── styles.css             # 🎨 Web styling
│   └── scripts.js             # ⚙️ Optional JS scripts for frontend

├── templates/                 # 🧾 HTML templates for Flask
│   ├── index.html             # Home page
│   ├── single_camera.html     # Upload page for single camera mode
│   ├── cross_camera.html      # Upload page for cross camera mode
│   ├── result_single.html     # Output view - single camera
│   └── result_cross.html      # Output view - cross camera

├── src/                       # 🧠 Core computer vision modules
│   ├── detect.py              # YOLOv11-based player detection
│   ├── extract_features.py    # Color histogram feature extractor
│   ├── match_cross_camera.py  # Cross-view identity matching logic
│   ├── track_single_camera.py # Player tracking with SORT
│   ├── combine_two_and_draw.py # Combine feeds and draw matched lines
│   └── utils.py               # Helper functions (drawing, I/O, etc.)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone "https://github.com/Gupta2002/player_reid_project"
cd player-reid-webapp
```

### 2️⃣ Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Place the YOLOv11 model
Place your trained YOLOv11 weights file (best.pt) inside the `models/` folder.

### 5️⃣ Run the app
```bash
python app.py
```
Then open your browser at: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Usage Instructions

➤ **Single Camera Mode**  
- Go to Single Camera Re-ID  
- Upload one video file(15sec_input_720p)
- View tracked player IDs in output video

➤ **Cross Camera Mode**  
- Go to Cross Camera Re-ID  
- Upload 2 vedio file(Broadcast, Tacticam)  
- See combined output with identity lines drawn

---

## 📊 Technologies Used

- Python 2.8+
- Flask
- OpenCV
- Ultralytics YOLOv11
- SORT Tracking
- NumPy & Matplotlib
- HTML/CSS (Jinja2 templates)

---

## 📎 Use Cases

- Broadcast production enhancement  
- Automated video analysis for sports coaches  
- Player tracking in soccer, basketball, etc.  
- Camera calibration research  
- Identity consistency validation across angles

---

## 📘 Report

For detailed methodology, evaluation, and results:  
📄 `docs/Project Report`

---

## 🙏 Acknowledgments

- Ultralytics YOLOv11  
- SORT Tracking  
- OpenCV community  
