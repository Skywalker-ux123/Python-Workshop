import cv2
from ultralytics import YOLO

print("🤖 Loading YOLO AI Model...")
# TODO: Initialize the YOLO model using "yolov8n.pt"
model = "YOUR_CODE_HERE"

print("📸 Starting Webcam...")
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # TODO: Pass the current 'frame' to the model to get 'results'
    results = "YOUR_CODE_HERE"

    # TODO: Plot the bounding boxes on the frame
    # Hint: Loop through the results and call .plot()
    for result in results:
        annotated_frame = "YOUR_CODE_HERE"

    # Show the video feed
    cv2.imshow("My First AI App", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()