🚀 Advanced AI Object Detection System
An AI-powered Object Detection System built using YOLOv8, Streamlit, and OpenCV.
This application detects objects in images, videos, and live webcam with real-time processing, object counting, voice alerts, and dashboard analytics.

📌 Features
Image Detection
Video Detection
Live Webcam Detection
Object Counting (Total + Object-wise)
Voice Alert System
Detection History Dashboard
Login Authentication System
Fast Detection using YOLOv8

🛠️ Tech Stack
Python
Streamlit
YOLOv8 (Ultralytics)
OpenCV
Pandas
Pillow (PIL)
pyttsx3

📁 Project Structure
project/
│
├── app.py
├── utils.py
├── auth.py
├── history.csv
├── requirements.txt

⚙️ Installation & Setup
cd ai-object-detection-system
Install Requirements
pip install -r requirements.txt
Run Project
streamlit run app.py

🔐 Login Credentials

Username: admin | Password: 1234
Username: student | Password: 1234

📊 How It Works

User logs in
Selects input type (Image / Video / Webcam)
YOLOv8 detects objects
Objects are counted
Voice alert is triggered
Data is saved in CSV
Dashboard shows analytics

🚀 Advantages

Real-time detection
Easy-to-use interface
Lightweight model
Multi-input support

⚠️ Limitations

Basic authentication
CSV storage (not scalable)
Requires internet for first-time model download

🔮 Future Improvements

Database integration (MySQL / Firebase)
Cloud deployment
Object tracking
Custom trained models

📦 Requirements

ultralytics
streamlit
opencv-python
pillow
numpy
pandas
matplotlib
pyttsx3

