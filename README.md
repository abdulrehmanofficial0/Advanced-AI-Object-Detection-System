Advanced AI Object Detection System
Project Description

The Advanced AI Object Detection System is a Computer Vision based project that detects objects in images, videos, and live webcam feeds using a deep learning model.

This system provides real-time detection, object counting, voice alerts, and data visualization through an interactive interface.

This project includes:

Real-Time Object Detection
Image, Video, and Webcam Processing
Object Counting System
Voice Alert System
Detection History Storage
Dashboard Visualization
Authentication System (Login/Logout)
Features

🔍 Image Object Detection
🎥 Video Object Detection
📷 Live Webcam Detection
🔢 Object Counting (Total + Object-wise)
🔊 Voice Alert System
📊 Detection History Dashboard
🔐 Login System
⚡ Fast Processing using YOLOv8

🧠 Machine Learning Model

Model: YOLOv8 (Ultralytics)
Task: Object Detection
Pre-trained Model: yolov8n.pt
Framework: PyTorch

📂 Project Structure

AI-Object-Detection-System/
│
├── app.py
├── utils.py
├── auth.py
├── history.csv
├── requirements.txt

Installation
1. Install Dependencies

pip install ultralytics streamlit opencv-python pillow numpy pandas matplotlib pyttsx3

How to Run
Run Streamlit App

streamlit run app.py

🔐 Login Credentials

Username: admin | Password: 1234
Username: student | Password: 1234

System Workflow
User logs into the system
Selects detection mode (Image / Video / Webcam)
YOLOv8 model processes the input
Objects are detected and counted
Voice alert is triggered when objects are detected
Detection data is saved in CSV file
Dashboard displays analytics
Output
Detected image/video with bounding boxes
Total object count
Object-wise count
Real-time detection display
Graph of detection history
Data Handling

Detection results are stored in:

history.csv

Each record contains:

Timestamp
Number of detected objects
Technologies Used

Python
Streamlit
YOLOv8 (Ultralytics)
OpenCV
Pandas
Pillow (PIL)
pyttsx3

Example Output

Objects Detected: 5
Person: 2
Car: 2
Dog: 1

Limitations
Basic authentication system
CSV storage is not scalable
Model accuracy depends on pretrained weights
No cloud deployment
Future Improvements

User Authentication with Database
Cloud Deployment (AWS / Render)
Object Tracking System
Custom Trained Models
Mobile Application
Advanced UI (React / Tailwind)
