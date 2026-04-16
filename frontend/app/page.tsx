"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select an image");
      return;
    }

    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post(
        "https://image-origin-finder-4.onrender.com/upload",
        formData
      );
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Error uploading image");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-pink-100 via-purple-100 to-blue-100 p-6">

      {/* Title */}
      <h1 className="text-4xl font-bold mb-6 text-purple-700">
        Image Origin Finder ✨
      </h1>

      {/* Upload Card */}
      <div className="bg-white/80 backdrop-blur-lg shadow-xl rounded-3xl p-6 w-full max-w-md text-center border border-white/50">

        {/* Drag & Drop */}
        <div
          className="border-2 border-dashed border-purple-300 rounded-xl p-6 mb-4 cursor-pointer hover:bg-purple-50 transition"
          onClick={() => document.getElementById("fileInput")?.click()}
        >
          <p className="text-gray-700">
            Drag & drop an image here or click to upload 📂
          </p>

          <input
            id="fileInput"
            type="file"
            className="hidden"
            onChange={(e) => {
              if (e.target.files && e.target.files[0]) {
                setFile(e.target.files[0]);
                setPreview(URL.createObjectURL(e.target.files[0]));
              }
            }}
          />
        </div>

        {/* Upload Button */}
        <button
          onClick={handleUpload}
          className="bg-gradient-to-r from-pink-400 to-purple-400 hover:scale-105 transition transform text-white px-4 py-2 rounded-xl w-full shadow-md"
        >
          Upload Image 🚀
        </button>

        {/* Loading */}
        {loading && (
          <p className="mt-4 text-purple-600 animate-pulse font-medium">
            ✨ Analyzing your image...
          </p>
        )}
      </div>

      {/* Preview + Results */}
      <div className="flex flex-col md:flex-row gap-6 mt-8 w-full max-w-4xl">

        {/* Image Preview */}
        {preview && (
          <img
            src={preview}
            alt="preview"
            className="w-full md:w-1/2 h-64 object-cover rounded-xl shadow-lg"
          />
        )}

        {/* Results */}
        {result && (
          <div className="w-full md:w-1/2">

            {/* Origin */}
            <div className="bg-green-200/80 backdrop-blur-md shadow-lg rounded-2xl p-4 mb-4 border border-green-300">
              <h2 className="text-xl font-semibold mb-2 text-green-800">
                🌍 Estimated Origin
              </h2>
              <p className="text-gray-900 font-medium">
                {result.estimated_origin?.source} (
                {result.estimated_origin?.date})
              </p>
            </div>

            {/* Matches */}
            <div className="bg-blue-200/80 backdrop-blur-md shadow-lg rounded-2xl p-4 border border-blue-300">
              <h2 className="text-xl font-semibold mb-3 text-blue-800">
                🔍 Similar Images
              </h2>

              {result.matches?.map((item: any, index: number) => (
                <div
                  key={index}
                  className="bg-white rounded-xl p-3 mb-3 hover:scale-[1.02] transition shadow-md border border-gray-200"
                >
                  <p className="text-gray-800">
                    <b>Image:</b> {item.image}
                  </p>

                  {/* Similarity Bar */}
                  <div className="mt-2">
                    <div className="w-full bg-gray-200 rounded-full h-2">
                      <div
                        className="bg-purple-400 h-2 rounded-full"
                        style={{ width: `${item.similarity * 100}%` }}
                      ></div>
                    </div>
                    <p className="text-sm text-gray-600 mt-1">
                      {(item.similarity * 100).toFixed(1)}%
                    </p>
                  </div>

                  <p className="text-gray-800">
                    <b>Source:</b> {item.source}
                  </p>
                  <p className="text-gray-800">
                    <b>Date:</b> {item.date}
                  </p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
