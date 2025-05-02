# 🎥 Video Anomaly Detection App

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Object%20Detection-green)](https://opencv.org/)

A lightweight, end-to-end **AI-powered video anomaly detection system** built using Streamlit and YOLOv8. Upload any video, run real-time object detection, detect anomalies, generate reports, and even receive alert notifications — all from a browser!

👉 **Live Demo**: [Open App](https://video-anomaly-detection-4nzsycjvlyk2mfw2xzuvpd.streamlit.app/)

---

## 📌 Features

- ✅ Upload and analyze custom videos
- 🚀 Real-time object detection using **YOLOv8**
- 📊 Anomaly detection and event logging
- 🧾 Downloadable CSV report of detected anomalies
- 📬 Email alert system for critical events (optional)
- 🧠 Modular and clean codebase
- ☁️ Deployed on **Streamlit Cloud**

---

## 📽️ Demo

https://user-images.githubusercontent.com/your-username/demo-video.mp4  
*(Replace with your actual demo link or GIF)*

---

## 📁 Project Structure

video-anomaly-detection/
├── main.py # Streamlit app frontend
├── detect.py # Core logic for YOLOv8 video detection
├── report.py # Anomaly analysis + CSV report generation
├── requirements.txt # Python dependencies
├── packages.txt # System-level dependency (libGL for OpenCV)
└── README.md # You're reading it!



---

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/Vivek7987/video-anomaly-detection.git
cd video-anomaly-detection
```
### 2. Install dependencies
```
pip install -r requirements.txt
```
### 3. Run the app
``` bash
streamlit run main.py
```
## 🚀 Deployment (on Streamlit Cloud)
1. Push your code to GitHub.
2. Go to streamlit.io/cloud.
3. Connect your GitHub repo and deploy it.
4. Make sure packages.txt contains:
```
libgl1-mesa-glx
```
This ensures OpenCV works on Streamlit Cloud.

## Model Used
- ### YOLOv8 by Ultralytics

- Pre-trained object detection model

- Fast and efficient on video streams

## 📬 Email Alert (Optional Feature)
You can enable email alerts for specific anomalies by configuring SMTP in main.py.

### 🔐 .gitignore Suggestion
gitignore
```
*.pkl
__pycache__/
*.csv
*.mp4
.env
```
### 🤖 Future Enhancements
- Add anomaly classification (normal vs abnormal behavior)
- Add support for multiple video formats
- Integrate a dashboard for historical anomaly trends
- Use Streamlit's session_state for better UX

### 🙋‍♂️ Author
Vivek Pal
📧 paljivivek12@gmail.com
🔗 LinkedIn | GitHub






