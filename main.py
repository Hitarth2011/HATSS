from face_utils import get_face_embedding
from clustering import FaceCluster
from alert import send_alert

# Create system object
face_system = FaceCluster()

# TRAINING PHASE
known_images = [
    "data/known/person1.jpg",
    "data/known/person2.jpg"
]

known_embeddings = []
for img in known_images:
    emb = get_face_embedding(img)
    if emb is not None:
        known_embeddings.append(emb)

face_system.train(known_embeddings)

# 🔥 ADD THIS FUNCTION (DO NOT REMOVE ABOVE CODE)
def run_detection(image_path):
    new_face = get_face_embedding(image_path)

    if new_face is None:
        return "No face detected"

    if face_system.is_known(new_face):
        return "Known"
    else:
        send_alert()
        return "Unknown"

# OPTIONAL: for manual testing
if __name__ == "__main__":
    result = run_detection("data/test/unknown.jpg")
    print(result)
