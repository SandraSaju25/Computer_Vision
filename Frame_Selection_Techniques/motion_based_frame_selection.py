#  Select high motion frames using OpenCV
import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")
prev_frame = None
selected_frame = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if prev_frame is not None:
        diff = cv2.absdiff(prev_frame, gray)
        motion_score = np.sum(diff)
        if motion_score > 1ef:
            selected_frames.append(frame)
    prev_frame = gray

cap.release()
