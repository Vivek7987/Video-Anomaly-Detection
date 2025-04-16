import cv2
import torch
from ultralytics import YOLO
import numpy as np
from report import generate_report
# Load YOLOv8 Model
model = YOLO("yolov8n.pt")  # Pretrained YOLOv8

def detect_objects(frame):
    """Detects objects in a given video frame."""
    results = model(frame)
    return results

def process_video(video_path):
    """Process video file for anomaly detection."""
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = detect_objects(frame)
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2, conf, cls = box.xyxy[0]
                print(f"Detected object: {cls} with confidence {conf}")  # Debugging
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

        cv2.imshow("Anomaly Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# def process_live_video():
#     """Process live video stream for anomaly detection."""
#     cap = cv2.VideoCapture(0)  # Use 0 for webcam or RTSP URL for IP camera

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Detect objects
#         results = model(frame)

#         # Check for anomalies (e.g., unauthorized person)
#         for result in results:
#             for box in result.boxes:
#                 cls = int(box.cls[0])
#                 conf = float(box.conf[0])
#                 if cls == 0 and conf > 0.5:  # Example: Class 0 is "person"
#                     print("Anomaly detected: Unauthorized person")
#                     # Trigger report generation
#                     report = generate_report("Unauthorized person detected in restricted area.")
#                     print("Generated Report:\n", report)

#         # Display the frame
#         cv2.imshow("Live Anomaly Detection", frame)
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# # Run live video processing
# process_live_video()