import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Load model (only once)
model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

def extract_features(img_path):
    # Load image
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    
    # Expand dimensions
    img = np.expand_dims(img, axis=0)
    
    # Preprocess
    img = preprocess_input(img)
    
    # Extract features
    features = model.predict(img)
    
    return features.flatten()