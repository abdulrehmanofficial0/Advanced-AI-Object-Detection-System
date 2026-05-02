import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import pandas as pd
from utils import count_objects, save_history, draw_info, object_wise_count
from auth import login, check_login
import threading
import pyttsx3
import tempfile


st.set_page_config(page_title="AI Detection System", layout="wide")
st.title("🧠 Advanced AI Object Detection System")


def speak(text):
    def run():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()


login()
if not check_login():
    st.warning("Please login to continue")
    st.stop()

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

if "alerted" not in st.session_state:
    st.session_state.alerted = False


menu = st.sidebar.radio("Menu", ["Image", "Webcam", "Video", "Dashboard"])


if menu == "Image":
    st.header("📷 Image Detection")

    file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

    if file:
        img = Image.open(file)
        st.image(img, caption="Original Image", use_column_width=True)

        if st.button("Detect"):
            results = model(img)
            output = results[0].plot()

            count = count_objects(results)
            obj_counts = object_wise_count(results, model)

            save_history(count)

            st.image(output, caption="Detected Image", use_column_width=True)
            st.success(f"Total Objects: {count}")

            st.subheader("📊 Object-wise Count")
            st.write(obj_counts)

            
            if count > 0 and not st.session_state.alerted:
                speak("Object detected")
                st.session_state.alerted = True
            if count == 0:
                st.session_state.alerted = False


elif menu == "Webcam":
    st.header("🎥 Live Detection")

    run = st.checkbox("Start Camera")
    frame_window = st.image([])
    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Camera not working")
            break

        results = model(frame)
        output = results[0].plot()

        count = count_objects(results)
        obj_counts = object_wise_count(results, model)

        output = draw_info(output, count)
        save_history(count)

        frame_window.image(output, channels="BGR")

        st.sidebar.write("Object Count:", obj_counts)

        if count > 0 and not st.session_state.alerted:
            speak("Object detected")
            st.session_state.alerted = True
        if count == 0:
            st.session_state.alerted = False

    cap.release()


elif menu == "Video":
    st.header("🎬 Video Detection")

    video_file = st.file_uploader("Upload Video", type=["mp4","avi","mov"])

    if video_file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())

        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)
            output = results[0].plot()

            count = count_objects(results)
            obj_counts = object_wise_count(results, model)

            output = draw_info(output, count)
            save_history(count)

            stframe.image(output, channels="BGR")
            st.sidebar.write("Object Count:", obj_counts)

            
            if count > 0 and not st.session_state.alerted:
                speak("Object detected in video")
                st.session_state.alerted = True
            if count == 0:
                st.session_state.alerted = False

        cap.release()


elif menu == "Dashboard":
    st.header("📊 Detection History")

    try:
        df = pd.read_csv("history.csv", names=["Time","Objects"])
        st.dataframe(df)

        st.subheader("📈 Graph")
        st.line_chart(df["Objects"])
    except:
        st.warning("No data yet")