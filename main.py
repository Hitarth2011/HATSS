from face_utils import get_face_embedding
from clustering import FaceCluster
from alert import send_alert
import os

# Initialize system
face_system = FaceCluster()

# TRAINING PHASE
def train_system():
    known_embeddings = []
    known_dir = "data/known"

    for img_name in os.listdir(known_dir):
        img_path = os.path.join(known_dir, img_name)
        emb = get_face_embedding(img_path)
        if emb is not None:
            known_embeddings.append(emb)

    if known_embeddings:
        face_system.train(known_embeddings)

train_system()

# 🔥 ADDED FUNCTION (THIS IS THE KEY CHANGE)
def run_detection(image_path):
    new_face = get_face_embedding(image_path)

    if new_face is None:
        return "No face detected"

    if face_system.is_known(new_face):
        return "Known"
    else:
        send_alert()
        return "Unknown"

# Optional local test
if __name__ == "__main__":
    print(run_detection("data/test/test.jpg"))
