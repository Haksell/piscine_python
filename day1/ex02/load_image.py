from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    """Load an image from a file into a numpy array."""
    try:
        img = Image.open(path)
        print("Image format:", img.format)
        img_array = np.array(img)
        print("The shape of image is:", img_array.shape)
        return img_array
    except FileNotFoundError:
        print("Error: The file does not exist.")
        return None
    except IOError:
        print("Error: The image file could not be read.")
        return None
