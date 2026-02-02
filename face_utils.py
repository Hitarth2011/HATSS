import mediapipe as mp
import numpy as np
from PIL import Image

mp_face_detection = mp.solutions.face_detection

def get_face_embedding(image_path):
    image = Image.open(image_path).convert("RGB")
    image_np = np.array(image)

    with mp_face_detection.FaceDetection(
        model_selection=0,
        min_detection_confidence=0.5
    ) as detector:

        results = detector.process(image_np)

        if not results or not results.detections:
            return None

        bbox = results.detections[0].location_data.relative_bounding_box

        # Lightweight numeric representation (stable for demo)
        embedding = np.array([
            bbox.xmin,
            bbox.ymin,
            bbox.width,
            bbox.height
        ])

        return embedding
