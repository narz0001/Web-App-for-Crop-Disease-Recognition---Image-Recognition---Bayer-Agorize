import os
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import resize
import numpy as np

def prepare_data(home, fruit, categories):
    data_input = []
    data_target = []

    for key in categories:
        category_path = os.path.join(home, fruit, key)
        os.chdir(category_path)
        for each in os.listdir('.'):
            # Check if the file has a valid image file extension
            valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff']
            if any(each.lower().endswith(ext) for ext in valid_extensions):
                image = io.imread(each)
                resize_img = resize(image, (200, 200))
                rgb_image = rgb2gray(resize_img)
                data_input.append(rgb_image.flatten().tolist())
                data_target.append(key)
        os.chdir(home)

    return np.array(data_input), np.array(data_target)
