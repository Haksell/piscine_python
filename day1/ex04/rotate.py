import sys
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load

FILENAME = "animal.jpeg"
ZOOM_SCALE = 0.6


def zoom_image(img_array: np.ndarray, scale: float) -> np.ndarray:
    """Return a zoomed, grayscale image."""
    width = img_array.shape[1]
    height = img_array.shape[0]
    center_x = width // 2
    center_y = height // 2
    half_square = round(min(img_array.shape[0], width) * scale * 0.5)
    zoomed_array = img_array[
        center_y - half_square : center_y + half_square,
        center_x - half_square : center_x + half_square,
    ]
    return np.dot(
        zoomed_array[:, :, :3],
        [0.299, 0.587, 0.114],
    )


def transpose_image(img_array: np.ndarray) -> np.ndarray:
    """Return a transposed image."""
    transposed_array = np.zeros((img_array.shape[1], img_array.shape[0]))
    for y in range(img_array.shape[0]):
        for x in range(img_array.shape[1]):
            transposed_array[x][y] = img_array[y][x]
    return transposed_array


def main():
    """Display a zoomed version of animal.jpeg."""
    img_array = ft_load(FILENAME)
    if img_array is None:
        sys.exit(1)
    print(img_array)
    zoomed_array = zoom_image(img_array, ZOOM_SCALE)
    transposed_array = transpose_image(zoomed_array)
    print("New shape after Transpose:", transposed_array.shape)
    print(transposed_array)
    plt.imshow(transposed_array, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
