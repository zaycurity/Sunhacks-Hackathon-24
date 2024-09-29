import cv2
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions

model = MobileNetV2(weights='imagenet')

def recognize_objects_in_frame(frame):
    try:
        # Resizes and preprocess the frame
        img_resized = cv2.resize(frame, (224, 224))
        img_preprocessed = preprocess_input(np.expand_dims(img_resized, axis=0))
        
        # Make predictions
        predictions = model.predict(img_preprocessed)
        
        decoded_preds = decode_predictions(predictions, top=3)[0]
        
        label = f"{decoded_preds[0][1]}: {decoded_preds[0][2]:.2f}"
        
        return label
    except Exception as e:
        print(f"Error during processing: {e}")
        return None

def real_time_object_detection():
    
    cap = cv2.VideoCapture(0)  # 0 for the default webcam, change if using external cameras

    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return
    
    while True:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            print("Failed to capture frame from webcam.")
            break
        
        label = recognize_objects_in_frame(frame)
        
        if label:
            cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        cv2.imshow("Real-Time Object Detection", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

real_time_object_detection()