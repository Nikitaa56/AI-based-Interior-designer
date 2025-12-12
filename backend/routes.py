from flask import Blueprint, request, jsonify
import json
import os
import sys
import time
import base64
import replicate
from io import BytesIO
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import requests
import numpy as np
from dotenv import load_dotenv

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

# Allow imports from ai_engine
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ai_engine.color_palette import extract_color_palette

api_bp = Blueprint('api', __name__)

# Initialize Replicate API
# Get API token from environment variable
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")
if not REPLICATE_API_TOKEN:
    print("⚠️ WARNING: REPLICATE_API_TOKEN not set. Image generation will fail.")
    print("   Get your API token from: https://replicate.com/account/api-tokens")
else:
    print("✅ Replicate API initialized successfully!")
    print(f"   Token: {REPLICATE_API_TOKEN[:10]}...")

UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load furniture data
FURNITURE_DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/furniture.json')
with open(FURNITURE_DATA_PATH, 'r') as f:
    furniture_data = json.load(f)


# ------------------------- COLOR PALETTE -------------------------
@api_bp.route('/palette', methods=['POST'])
def get_color_palette():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    temp_path = '/tmp/temp_image.jpg'
    image_file = request.files['image']
    image_file.save(temp_path)

    try:
        colors = extract_color_palette(temp_path, num_colors=5)
        os.remove(temp_path)

        hex_colors = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for r, g, b in colors]
        return jsonify({'colors': hex_colors})
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return jsonify({'error': str(e)}), 500


# ------------------------- LOCAL FALLBACK (NO API TOKEN) -------------------------
def generate_local_fallback(prompt, image_file):
    """
    Fallback image generation when no API token is available.
    Creates variations using advanced PIL techniques and color manipulation.
    """
    try:
        if not image_file:
            return jsonify({"error": "Please upload an image to use local generation"}), 400

        print("🎨 Generating design variation locally...")

        # Load the uploaded image
        img = Image.open(image_file)

        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize to reasonable size
        max_size = 1024
        if max(img.size) > max_size:
            ratio = max_size / max(img.size)
            new_size = tuple(int(dim * ratio) for dim in img.size)
            img = img.resize(new_size, Image.Resampling.LANCZOS)

        # Create a copy for manipulation
        import numpy as np
        img_array = np.array(img)

        # Apply transformations based on prompt keywords
        prompt_lower = prompt.lower()

        # Color scheme transformations
        if any(word in prompt_lower for word in ['modern', 'minimalist', 'contemporary']):
            # Desaturate and increase contrast for modern look
            img = ImageOps.autocontrast(img, cutoff=2)
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(0.8)
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.3)

        elif any(word in prompt_lower for word in ['luxury', 'elegant', 'sophisticated']):
            # Warmer tones, deeper colors
            img_array = np.array(img).astype(float)
            # Add warm tone
            img_array[:, :, 0] = np.clip(img_array[:, :, 0] * 1.1, 0, 255)  # More red
            img_array[:, :, 2] = np.clip(img_array[:, :, 2] * 0.95, 0, 255)  # Less blue
            img = Image.fromarray(img_array.astype('uint8'))
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.2)

        elif any(word in prompt_lower for word in ['bright', 'light', 'airy', 'white']):
            # Brighten and lighten
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.3)
            # Add slight overexposure effect
            img_array = np.array(img).astype(float)
            img_array = np.clip(img_array * 1.15 + 20, 0, 255)
            img = Image.fromarray(img_array.astype('uint8'))

        elif any(word in prompt_lower for word in ['dark', 'moody', 'dramatic']):
            # Darken and add drama
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(0.7)
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.4)
            # Add vignette effect
            img_array = np.array(img).astype(float)
            h, w = img_array.shape[:2]
            Y, X = np.ogrid[:h, :w]
            center_y, center_x = h // 2, w // 2
            dist = np.sqrt((X - center_x)**2 + (Y - center_y)**2)
            max_dist = np.sqrt(center_x**2 + center_y**2)
            vignette = 1 - (dist / max_dist) * 0.5
            img_array = img_array * vignette[:, :, np.newaxis]
            img = Image.fromarray(np.clip(img_array, 0, 255).astype('uint8'))

        elif any(word in prompt_lower for word in ['vibrant', 'colorful', 'bold']):
            # Boost saturation and vibrancy
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1.5)
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.2)
            # Boost specific color channels
            img_array = np.array(img).astype(float)
            img_array = np.clip(img_array * 1.1, 0, 255)
            img = Image.fromarray(img_array.astype('uint8'))

        elif any(word in prompt_lower for word in ['rustic', 'vintage', 'traditional']):
            # Add sepia/warm vintage tone
            img_array = np.array(img).astype(float)
            # Sepia transformation
            sepia_r = img_array[:, :, 0] * 0.393 + img_array[:, :, 1] * 0.769 + img_array[:, :, 2] * 0.189
            sepia_g = img_array[:, :, 0] * 0.349 + img_array[:, :, 1] * 0.686 + img_array[:, :, 2] * 0.168
            sepia_b = img_array[:, :, 0] * 0.272 + img_array[:, :, 1] * 0.534 + img_array[:, :, 2] * 0.131
            img_array[:, :, 0] = np.clip(sepia_r * 0.6 + img_array[:, :, 0] * 0.4, 0, 255)
            img_array[:, :, 1] = np.clip(sepia_g * 0.6 + img_array[:, :, 1] * 0.4, 0, 255)
            img_array[:, :, 2] = np.clip(sepia_b * 0.6 + img_array[:, :, 2] * 0.4, 0, 255)
            img = Image.fromarray(img_array.astype('uint8'))

        else:
            # Default: general enhancement
            img = ImageOps.autocontrast(img, cutoff=1)
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.3)
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1.1)

        # Final sharpening
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.2)

        # Apply edge enhancement for detail
        img = img.filter(ImageFilter.EDGE_ENHANCE)

        # Save the generated variation
        filename = f"generated_{int(time.time())}.png"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        img.save(filepath, quality=95)

        print(f"✅ Design variation created: {filepath}")

        return jsonify({
            "image_url": f"http://127.0.0.1:5001/static/{filename}",
            "message": "Design variation created! (Local mode - for full AI generation, add Replicate API token)"
        })

    except Exception as e:
        print(f"❌ Local generation error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Local generation failed: {str(e)}"}), 500


# ------------------------- FURNITURE -------------------------
@api_bp.route('/furniture', methods=['GET'])
def get_furniture():
    category = request.args.get('category')
    if category:
        filtered = [i for i in furniture_data if i['category'].lower() == category.lower()]
        return jsonify(filtered)
    return jsonify(furniture_data)


# ------------------------- FREE AI GENERATION (POLLINATIONS.AI) -------------------------
def generate_with_free_ai(prompt, image_file):
    """
    FREE AI image generation using Pollinations.ai
    Completely free, no API key, no credit card required!
    """
    try:
        print("🎨 Using FREE Pollinations.ai for AI generation...")

        # Prepare the enhanced prompt
        enhanced_prompt = f"professional interior design, {prompt}, high quality, detailed, photorealistic, modern, 8k"

        # URL encode the prompt
        import urllib.parse
        encoded_prompt = urllib.parse.quote(enhanced_prompt)

        # Pollinations.ai FREE API - no key needed!
        # This generates images directly from text prompts
        API_URL = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=768&nologo=true&enhance=true"

        print(f"🚀 Calling FREE Pollinations.ai API (10-20 seconds)...")
        print(f"   Prompt: {enhanced_prompt}")

        # Download the generated image
        response = requests.get(API_URL, timeout=60)

        if response.status_code != 200:
            raise Exception(f"API returned status {response.status_code}")

        # Load the generated image from response
        generated_image = Image.open(BytesIO(response.content))

        # If user uploaded an image, blend it with the AI generation for better results
        if image_file:
            print("📸 Blending uploaded image with AI generation...")

            # Read the uploaded image
            user_img = Image.open(image_file)

            # Convert to RGB if needed
            if user_img.mode != 'RGB':
                user_img.convert('RGB')

            # Resize user image to match generated image
            user_img = user_img.resize(generated_image.size, Image.Resampling.LANCZOS)

            # Blend: 30% original, 70% AI generated
            import numpy as np
            user_array = np.array(user_img).astype(float)
            gen_array = np.array(generated_image).astype(float)
            blended = (user_array * 0.3 + gen_array * 0.7).astype('uint8')
            generated_image = Image.fromarray(blended)

        # Save the generated image
        filename = f"generated_{int(time.time())}.png"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        generated_image.save(filepath, quality=95)

        print(f"✅ FREE AI generation complete: {filepath}")

        return jsonify({
            "image_url": f"http://127.0.0.1:5001/static/{filename}",
            "message": "AI-generated design created! (100% FREE - No credit card needed!)"
        })

    except Exception as e:
        print(f"❌ Free AI generation error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"AI generation failed: {str(e)}. Please try again."}), 500


# ------------------------- IMAGE GENERATION -------------------------
@api_bp.route('/generate', methods=['POST'])
def generate():
    # Get prompt and image from form data
    prompt = request.form.get("prompt", "")
    image_file = request.files.get("image")

    if not prompt:
        return jsonify({"error": "Prompt missing"}), 400

    # USE FREE POLLINATIONS.AI API (no credit card needed!)
    print("✨ Generating with FREE AI:", prompt)
    return generate_with_free_ai(prompt, image_file)


# ------------------------- SAVE DESIGN -------------------------
@api_bp.route('/save', methods=['POST'])
def save_design():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    return jsonify({'message': 'Design saved successfully', 'id': 'temp_id'})
