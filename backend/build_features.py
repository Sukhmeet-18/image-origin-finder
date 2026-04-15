import os
import json
import numpy as np
from backend.feature_extractor import extract_features

DATASET_PATH = "../dataset"
IMAGE_FOLDER = os.path.join(DATASET_PATH, "images")
METADATA_FILE = os.path.join(DATASET_PATH, "metadata.json")

# Load metadata
with open(METADATA_FILE, "r") as f:
    metadata = json.load(f)

features_list = []
image_paths = []

print("Extracting features...")

for item in metadata:
    img_name = item["image"]
    img_path = os.path.join(IMAGE_FOLDER, img_name)

    if os.path.exists(img_path):
        features = extract_features(img_path)
        features_list.append(features)
        image_paths.append(img_name)
    else:
        print(f"Missing: {img_name}")

# Convert to numpy array
features_array = np.array(features_list)

# Save features + image names
np.save("features.npy", features_array)
np.save("image_names.npy", np.array(image_paths))

print("Features saved successfully ✅")
print("Shape:", features_array.shape)
