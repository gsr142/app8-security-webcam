import cv2
import streamlit as st
from datetime import datetime
st.title("Motion Detector")
start = st.button("Start Camera")
now = datetime.now()
day = now.strftime("%A")
dt_string = now.strftime("%H:%M:%S")
if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text=day, org=(10, 30),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(250, 100, 200), thickness=2, lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=dt_string, org=(10,70),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(20, 100, 200), thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)