from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
import shutil
import os

from backend.similarity_search import find_similar_images
from origin_estimator import estimate_origin

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "Image Origin API Running 🚀"}


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Step 1: Find similar images
    results = find_similar_images(file_path)

    # Step 2: Estimate origin
    origin = estimate_origin(results)

    return {
        "matches": results,
        "estimated_origin": origin
    }
