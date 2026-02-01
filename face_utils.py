import cv2
import mediapipe as mp
import numpy as np

mp_face_detection = mp.solutions.face_detection

def get_face_embedding(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_face_detection.FaceDetection(model_selection=1,
                                         min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(image_rgb)

        if not results.detections:
            return None

        # Use bounding box as simple embedding proxy
        bbox = results.detections[0].location_data.relative_bounding_box
        return np.array([
            bbox.xmin,
            bbox.ymin,
            bbox.width,
            bbox.height
        ])
