# 🖼️ Image Origin Finder

A full-stack machine learning application that identifies the probable origin of an image using deep learning and similarity search.

---

## 🚀 Live Demo

* 🔗 Frontend: https://your-vercel-link.vercel.app
* 🔗 Backend API: https://image-origin-finder-4.onrender.com

---

## 🧠 What This Project Does

* Upload any image
* Extract features using a deep learning model (MobileNetV2)
* Compare with a dataset using cosine similarity
* Return the most similar images along with metadata
* Estimate the origin/source of the image

---

## 🏗️ Tech Stack

### 🔹 Frontend

* Next.js (React)
* Tailwind CSS

### 🔹 Backend

* FastAPI
* Uvicorn

### 🔹 Machine Learning

* TensorFlow (MobileNetV2)
* NumPy
* Scikit-learn (cosine similarity)

### 🔹 Deployment

* Frontend: Vercel
* Backend: Render

---

## ⚙️ Project Structure

```
image-origin-finder/
│
├── backend/
│   ├── main.py
│   ├── feature_extractor.py
│   ├── similarity_search.py
│   ├── features.npy
│   ├── image_names.npy
│
├── dataset/
│   ├── images/
│   ├── metadata.json
│
├── frontend/
│   ├── app/
│   ├── public/
│
└── README.md
```

---

## 🧪 How It Works

1. Image is uploaded via frontend
2. Backend extracts feature vector using MobileNetV2
3. Cosine similarity is computed against stored dataset features
4. Top matches are retrieved
5. Metadata is used to estimate origin

---

## 💻 Running Locally

### 1. Clone the repo

```
git clone https://github.com/your-username/image-origin-finder.git
cd image-origin-finder
```

---

### 2. Backend setup

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

### 3. Frontend setup

```
cd frontend
npm install
npm run dev
```

---

## ⚠️ Notes

* TensorFlow runs on CPU in deployment (no GPU)
* First request may be slow due to cold start (Render free tier)
* Large `.npy` files are precomputed for faster inference

---

## ✨ Future Improvements

* Show top 3 similar images
* Add similarity confidence score
* Improve UI/UX with animations
* Add drag-and-drop upload
* Optimize model performance

---

## 💼 Author

**Sukhmeet Kaur**

* Aspiring Data Scientist | ML Developer

---

## ⭐ If you found this useful

Give it a star and feel free to connect!
