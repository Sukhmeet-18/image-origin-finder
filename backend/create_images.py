from PIL import Image
import os

output_dir = "../dataset/images"
os.makedirs(output_dir, exist_ok=True)

for i in range(1, 501):  # 500 images
    img = Image.new('RGB', (224, 224), color=(i*5 % 255, i*3 % 255, i*7 % 255))
    img.save(f"{output_dir}/img{i}.jpg")

print("500 images created successfully ✅")