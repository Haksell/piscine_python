import numpy as np


def ft_invert(img: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    return 255 - img


def ft_red(img: np.ndarray) -> np.ndarray:
    """Select the red channel of an image."""
    return img * [1, 0, 0]


def ft_green(img: np.ndarray) -> np.ndarray:
    """Select the green channel of an image."""
    return img - ft_red(img) - ft_blue(img)


def ft_blue(img: np.ndarray) -> np.ndarray:
    """Select the blue channel of an image."""
    blue = img.copy()
    blue[:, :, :2] = 0
    return blue


def ft_grey(img: np.ndarray) -> np.ndarray:
    """Return the image in greyscale."""
    grey = np.dot(img[:, :, :3], [0.299, 0.587, 0.114])
    return np.stack([grey, grey, grey], axis=-1).astype(np.uint8)
