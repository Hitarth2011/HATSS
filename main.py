from face_utils import get_face_embedding
from clustering import FaceCluster
from alert import send_alert

face_system = FaceCluster()

# TRAINING PHASE
known_images = [
    "data/family1.jpg",
    "data/family2.jpg",
    "data/family3.jpg"
]

known_embeddings = []
for img in known_images:
    emb = get_face_embedding(img)
    if emb is not None:
        known_embeddings.append(emb)

face_system.train(known_embeddings)

# DETECTION PHASE
new_face = get_face_embedding("camera_frame.jpg")

if new_face is not None:
    if face_system.is_known(new_face):
        print("✅ Known person detected")
    else:
        send_alert()
