import numpy as np
from PIL import Image
import random

def flip_image(img):
    return np.flipud(np.fliplr(img))

def add_noise(img):
    noise = np.random.randint(0, 50, img.shape, dtype=np.uint8)
    return np.clip(img + noise, 0, 255)

def brighten_channels(img, value=40):
    return np.clip(img + value, 0, 255)

def apply_mask(img):
    h, w, _ = img.shape
    x, y = w // 2 - 50, h // 2 - 50
    img[y:y+100, x:x+100] = 0
    return img

def process_image(file_path, output_path):
    img = np.array(Image.open(file_path))
    img = flip_image(img)
    img = add_noise(img)
    img = brighten_channels(img)
    img = apply_mask(img)
    Image.fromarray(img).save(output_path)

process_image('images/birds.jpg', 'output.jpg')
