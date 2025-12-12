import React, { useState } from "react";
import "./App.css";
import { Upload, Loader2, Sparkles, Image as ImageIcon, Palette, Download } from "lucide-react";

function App() {
  const [prompt, setPrompt] = useState("");
  const [generatedImage, setGeneratedImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [palette, setPalette] = useState([]);
  const [selectedImage, setSelectedImage] = useState(null);
  const [previewImage, setPreviewImage] = useState(null);
  const [error, setError] = useState(null);

  // ---------------- Upload Handler ---------------- //
  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(file);
      // Create preview
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreviewImage(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  // ---------------- Generate AI Image ---------------- //
  const generateDesign = async () => {
    if (!prompt) {
      setError("Please enter a design prompt!");
      return;
    }

    setLoading(true);
    setError(null);
    setGeneratedImage(null);

    try {
      const formData = new FormData();
      formData.append("prompt", prompt);
      if (selectedImage) {
        formData.append("image", selectedImage);
      }

      const res = await fetch("/api/generate", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      if (res.ok) {
        setGeneratedImage(data.image_url);
        setError(null);
      } else {
        setError(data.error || "Failed to generate image");
      }
    } catch (err) {
      setError("Network error. Please check if the backend is running.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // ---------------- Extract Color Palette ---------------- //
  const extractPalette = async () => {
    if (!selectedImage) {
      setError("Please upload an image first!");
      return;
    }

    try {
      const formData = new FormData();
      formData.append("image", selectedImage);

      const res = await fetch("/api/palette", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      if (res.ok) {
        setPalette(data.colors);
        setError(null);
      } else {
        setError(data.error || "Failed to extract palette");
      }
    } catch (err) {
      setError("Failed to extract color palette");
      console.error(err);
    }
  };

  return (
    <div className="app-container">
      {/* ---------------- HEADER ---------------- */}
      <header className="header">
        <div className="header-content">
          <div className="logo">
            <Sparkles className="logo-icon" />
            <h1>AI Interior Designer</h1>
          </div>
          <p className="tagline">Transform your space with AI-powered design</p>
        </div>
      </header>

      {/* ---------------- MAIN CONTENT ---------------- */}
      <main className="main-content">
        <div className="container">

          {/* Error Message */}
          {error && (
            <div className="error-message">
              <p>{error}</p>
              <button onClick={() => setError(null)}>×</button>
            </div>
          )}

          {/* Input Section */}
          <div className="input-section">

            {/* Upload Card */}
            <div className="card upload-card">
              <div className="card-header">
                <Upload className="card-icon" />
                <h2>Upload Room Image</h2>
              </div>
              <div className="card-body">
                <label className="upload-zone">
                  <input
                    type="file"
                    accept="image/*"
                    onChange={handleFileUpload}
                    className="file-input"
                  />
                  {previewImage ? (
                    <div className="preview-container">
                      <img src={previewImage} alt="Preview" className="preview-image" />
                      <div className="preview-overlay">
                        <Upload size={24} />
                        <span>Change Image</span>
                      </div>
                    </div>
                  ) : (
                    <div className="upload-placeholder">
                      <Upload size={48} />
                      <p className="upload-text">Click to upload or drag & drop</p>
                      <p className="upload-hint">PNG, JPG up to 10MB</p>
                    </div>
                  )}
                </label>
              </div>
            </div>

            {/* Prompt Card */}
            <div className="card prompt-card">
              <div className="card-header">
                <ImageIcon className="card-icon" />
                <h2>Describe Your Vision</h2>
              </div>
              <div className="card-body">
                <textarea
                  className="prompt-textarea"
                  placeholder="Describe your dream interior design... e.g., 'Modern minimalist living room with natural light, wooden furniture, and plants'"
                  value={prompt}
                  onChange={(e) => setPrompt(e.target.value)}
                  rows={4}
                />
                <button
                  className="generate-button"
                  onClick={generateDesign}
                  disabled={loading}
                >
                  {loading ? (
                    <>
                      <Loader2 className="spin" size={20} />
                      <span>Generating...</span>
                    </>
                  ) : (
                    <>
                      <Sparkles size={20} />
                      <span>Generate Design</span>
                    </>
                  )}
                </button>
              </div>
            </div>
          </div>

          {/* Results Section */}
          {generatedImage && (
            <div className="results-section">
              <div className="card result-card">
                <div className="card-header">
                  <ImageIcon className="card-icon" />
                  <h2>Generated Design</h2>
                  <a
                    href={generatedImage}
                    download
                    className="download-button"
                    title="Download Image"
                  >
                    <Download size={20} />
                  </a>
                </div>
                <div className="card-body">
                  <img
                    src={generatedImage}
                    alt="AI Generated Interior"
                    className="result-image"
                  />
                </div>
              </div>

              {/* Color Palette Card */}
              <div className="card palette-card">
                <div className="card-header">
                  <Palette className="card-icon" />
                  <h2>Color Palette</h2>
                </div>
                <div className="card-body">
                  <button
                    className="extract-button"
                    onClick={extractPalette}
                  >
                    Extract Colors
                  </button>
                  {palette.length > 0 && (
                    <div className="color-palette">
                      {palette.map((color, index) => (
                        <div key={index} className="color-item">
                          <div
                            className="color-swatch"
                            style={{ backgroundColor: color }}
                          />
                          <span className="color-code">{color}</span>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            </div>
          )}
        </div>
      </main>

      {/* ---------------- FOOTER ---------------- */}
      <footer className="footer">
        <p>© 2025 AI Interior Designer • Powered by Stable Diffusion</p>
      </footer>
    </div>
  );
}

export default App;
