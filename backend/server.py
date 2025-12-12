import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from routes import api_bp
from dotenv import load_dotenv

# Load environment variables from .env file in the backend directory
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)
print(f"🔍 Loading .env from: {env_path}")
print(f"🔑 API Token loaded: {os.environ.get('REPLICATE_API_TOKEN', 'NOT FOUND')[:20]}...")

app = Flask(__name__)
CORS(app)

# Static folder
UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# REGISTER ALL /api/... routes
app.register_blueprint(api_bp, url_prefix="/api")

@app.route("/")
def home():
    return "Backend running! 🚀"

# static files
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    # Use port 5001 to avoid conflict with macOS AirPlay on port 5000
    app.run(port=5001, debug=True, use_reloader=False)
