from similarity_search import find_similar_images
from origin_estimator import estimate_origin

query_image = "../dataset/images/img10.jpg"

# Step 1: get similar images
results = find_similar_images(query_image)

# Step 2: estimate origin
origin = estimate_origin(results)

print("\n--- Similar Images ---")
for i, res in enumerate(results, 1):
    print(f"{i}. {res['image']} | Similarity: {res['similarity']:.2f}")
    print(f"   Source: {res['source']} | Date: {res['date']}")

print("\n--- Estimated Origin ---")
print(origin)