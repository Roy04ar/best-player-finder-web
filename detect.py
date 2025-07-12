import cv2, os
from ultralytics import YOLO

def extract_frames_and_detect_players(video_path, save_dir="temp/frames"):
    os.makedirs(save_dir, exist_ok=True)
    model = YOLO("yolov8n.pt")  # Use YOLOv8 nano for speed
    cap = cv2.VideoCapture(video_path)

    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or count > 100:  # Limit to 100 frames
            break
        results = model(frame)
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = box.xyxy[0].int().tolist()
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.imwrite(f"{save_dir}/frame_{count:04d}.jpg", frame)
        count += 1
    cap.release()