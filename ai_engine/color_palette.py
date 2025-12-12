from PIL import Image
import numpy as np

def extract_color_palette(image_path, num_colors=5):
    """
    Extract dominant colors from an image using simple color quantization.
    Returns a list of RGB tuples.
    """
    try:
        img = Image.open(image_path)

        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize for faster processing
        img = img.resize((150, 150))

        # Use PIL's built-in quantize method for color extraction
        # This is much faster and doesn't require sklearn
        img_quantized = img.quantize(colors=num_colors)

        # Get the palette colors
        palette = img_quantized.getpalette()

        # Extract the dominant colors (first num_colors * 3 values)
        colors = []
        for i in range(num_colors):
            r = palette[i * 3]
            g = palette[i * 3 + 1]
            b = palette[i * 3 + 2]
            colors.append((r, g, b))

        return colors
    except Exception as e:
        print(f"Error extracting color palette: {e}")
        # Return some default colors if extraction fails
        return [(100, 100, 100), (150, 150, 150), (200, 200, 200), (50, 50, 50), (175, 175, 175)]
