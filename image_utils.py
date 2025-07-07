from PIL import Image
import numpy as np

def load_and_preprocess_image(image_file):
    img = Image.open(image_file).convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    return img_array
