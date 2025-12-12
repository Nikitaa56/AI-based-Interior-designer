# NestAI Interior Designer

A modern AI-powered interior design application that transforms room images using Stable Diffusion and provides design recommendations.

## Features

- **AI Image Generation**: Transform room photos into beautiful interior designs using Stable Diffusion
- **Style Selection**: Choose from various design styles (Modern, Minimalist, Industrial, Boho, Traditional)
- **Color Palette Extraction**: Automatically extract dominant colors from uploaded images
- **Before/After Comparison**: Interactive slider to compare original and generated designs
- **Furniture Recommendations**: Browse curated furniture collections
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## Project Structure

```
├── frontend/          # React frontend application
│   ├── src/
│   │   ├── components/    # Reusable React components
│   │   ├── App.js         # Main application component
│   │   └── index.js       # Application entry point
│   ├── public/            # Static assets
│   └── package.json       # Frontend dependencies
├── backend/           # Flask backend API
│   ├── server.py          # Main Flask application
│   ├── routes.py          # API route definitions
│   ├── static/            # Generated images storage
│   └── venv/              # Python virtual environment
├── ai_engine/         # AI processing modules
│   └── color_palette.py   # Color extraction utilities
├── data/              # Static data files
│   └── furniture.json     # Furniture catalog
└── docs/              # Documentation
    └── README.md          # This file
```

## Installation

### Prerequisites

- Python 3.8+
- Node.js 16+
- Git

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install flask flask-cors torch diffusers transformers accelerate pillow scikit-learn
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

## Usage

### Running the Application

1. Start the backend server:
   ```bash
   cd backend
   source venv/bin/activate
   python server.py
   ```

2. In a new terminal, start the frontend:
   ```bash
   cd frontend
   npm start
   ```

3. Open your browser and navigate to `http://localhost:3000`

### Using the Application

1. **Upload Image**: Click the file upload button to select a room photo
2. **Extract Colors** (Optional): Click "Extract Color Palette" to see dominant colors
3. **Choose Style**: Select a design style from the available options
4. **Add Prompt** (Optional): Enter additional design preferences
5. **Generate**: Click "Generate Design" to create your AI-transformed room
6. **Compare**: Use the before/after slider to compare results

## API Endpoints

### Backend API

- `POST /api/generate` - Generate interior design image
- `POST /api/palette` - Extract color palette from image
- `GET /api/furniture` - Get furniture recommendations
- `POST /api/save` - Save design (placeholder)

## Technologies Used

- **Frontend**: React, Tailwind CSS, Framer Motion
- **Backend**: Flask, Python
- **AI/ML**: Stable Diffusion, Hugging Face Transformers, scikit-learn
- **Image Processing**: PIL (Pillow)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Stable Diffusion model by Stability AI
- Hugging Face for model hosting
- React community for excellent documentation and tools
