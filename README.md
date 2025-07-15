  
# 🏃‍♂️ Player Re-Identification in Sports Footage (Web App)

## 📌 Project Overview

This web application enables **automated player re-identification** in sports videos using computer vision. It supports:

- **Single-Camera Re-ID**: Track players in a single video feed.
- **Cross-Camera Re-ID**: Match players across three video views (Broadcast, Tacticam) and generate a combined visual.

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
https://github.com/user-attachments/assets/42c83cb9-e960-4cc2-bed9-eefe5f5756ce

---

## ✍️ Report
[Project.Report.pdf](https://github.com/user-attachments/files/21175253/Project.Report.pdf)

---

## Demo Outputs Vedios
### 🎥 Cross Camera Outputs Vedio
https://github.com/user-attachments/assets/f8434468-c9d1-4958-8fa7-7500a34dec41
---

### 🎥 Single Camera Outputs Vedio
https://github.com/user-attachments/assets/261dc411-1ac5-4d78-837e-3bdbe446bd45
---

## 🖼️ Screenshots

### 🏠 Home Page  
> **Landing page of the system providing navigation to single or cross-camera modes.**
![Home](https://github.com/user-attachments/assets/bcabaf5d-a743-410e-bff8-a4d9d3c8014b)

### 📥 Upload Page (Single Camera)  
> **UI for uploading a single video for tracking players using YOLO and SORT.**
![Single Upload](https://github.com/user-attachments/assets/5af295b5-a05a-469c-9886-9fe221a653d3)

### 📥 Upload Page (Cross Camera)  
> **Three video inputs (Broadcast, Tacticam, Overview) accepted to perform identity matching across multiple angles.**
<img width="1366" height="768" alt="Screenshot (1015)" src="https://github.com/user-attachments/assets/f47778d2-614d-4fd7-bdb5-57181ea7b553" />

### 🎞️ Input Video (Single Camera)  
> **Original video from a single feed (e.g., Broadcast camera) to be processed for player tracking.**
![Input Single](https://github.com/user-attachments/assets/98d81273-16f7-4409-8933-00602df08b5e)

### 🧵 Output Video (Single Camera)  
> **Resulting video image showing tracked players with persistent IDs within the same camera.**
<img width="1366" height="618" alt="Screenshot (1020)" src="https://github.com/user-attachments/assets/e1221340-3ab4-4424-9a5c-dc3e237b901a" />

### 🎥 Input Videos (Cross Camera)  
> *Two videos used for multi-camera player re-identification:*
> - **Broadcast Camera View**
<img width="1366" height="748" alt="Screenshot (1016)" src="https://github.com/user-attachments/assets/c0ba5337-cc1a-48bb-aa7d-834329ebf5fe" />

> - **Tacticam Camera View**  
<img width="1366" height="544" alt="Screenshot (1017)" src="https://github.com/user-attachments/assets/2ad720f0-4025-4d61-ac4f-c2f846c4e165" />

### 🎯 Output Video (Cross Camera Combined)  
> **Final combined video image with identity lines drawn to represent matched players across views.**
<img width="1366" height="605" alt="Screenshot (1018)" src="https://github.com/user-attachments/assets/8623afef-e612-4f7e-bee2-8d06e98b1a72" />

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
│   ├── combine_three_and_draw.py # Combine feeds and draw matched lines
│   └── utils.py               # Helper functions (drawing, I/O, etc.)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone "https://github.com/Gupta3003/player_reid_project"
cd player-reid-webapp
```

### 2️⃣ Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 3️⃣ Install dependencies
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
- Upload one video file  
- View tracked player IDs in output video

➤ **Cross Camera Mode**  
- Go to Cross Camera Re-ID  
- Upload 2 views (Broadcast, Tacticam)  
- See combined output with identity lines drawn

---

## 📊 Technologies Used

- Python 3.8+
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
