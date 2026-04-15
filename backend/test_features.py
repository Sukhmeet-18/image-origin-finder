from backend.feature_extractor import extract_features

img_path = "../dataset/images/img1.jpg"

features = extract_features(img_path)

print("Feature vector length:", len(features))
print("First 10 values:", features[:10])
