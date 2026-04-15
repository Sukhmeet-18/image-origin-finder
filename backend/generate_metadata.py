import json
import random
from datetime import datetime, timedelta

# Possible sources
sources = [
    "Reddit", "Wikipedia", "Twitter", "BBC News",
    "Instagram", "Blog", "Unsplash", "Flickr"
]

metadata = []

base_date = datetime(2015, 1, 1)

for i in range(1, 501):
    random_days = random.randint(0, 3000)
    date = (base_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

    metadata.append({
        "image": f"img{i}.jpg",
        "source": random.choice(sources),
        "date": date
    })

# Save file
with open("../dataset/metadata.json", "w") as f:
    json.dump(metadata, f, indent=4)

print("metadata.json created successfully ✅")