import numpy as np
import os
import json
from sklearn.metrics.pairwise import cosine_similarity
from backend.feature_extractor import extract_features

# Load saved data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

features = np.load(os.path.join(BASE_DIR, "features.npy"))
image_names = np.load(os.path.join(BASE_DIR, "image_names.npy"))

# Load metadata
with open("../dataset/metadata.json", "r") as f:
    metadata = json.load(f)

# Convert metadata to dictionary for quick lookup
metadata_dict = {item["image"]: item for item in metadata}


def find_similar_images(query_image_path, top_k=5):
    # Extract features of query image
    query_features = extract_features(query_image_path)

    # Compute similarity
    similarities = cosine_similarity([query_features], features)[0]

    # Get top K indices
    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []

    for idx in top_indices:
        img_name = image_names[idx]
        similarity_score = float(similarities[idx])

        meta = metadata_dict.get(img_name, {})

        results.append({
            "image": img_name,
            "similarity": similarity_score,
            "source": meta.get("source", "Unknown"),
            "date": meta.get("date", "Unknown")
        })

    return results
