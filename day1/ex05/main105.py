import sys
import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def main():
    """Display the same image in 6 different filters."""
    img_array = ft_load("landscape.jpg")
    if img_array is None:
        sys.exit(1)

    fig, axs = plt.subplots(3, 2, figsize=(9, 6))

    axs[0, 0].imshow(img_array)
    axs[0, 0].set_title("Original")
    axs[0, 1].imshow(ft_invert(img_array))
    axs[0, 1].set_title("Invert")
    axs[1, 0].imshow(ft_red(img_array))
    axs[1, 0].set_title("Red")
    axs[1, 1].imshow(ft_green(img_array))
    axs[1, 1].set_title("Green")
    axs[2, 0].imshow(ft_blue(img_array))
    axs[2, 0].set_title("Blue")
    axs[2, 1].imshow(ft_grey(img_array))
    axs[2, 1].set_title("Grey")

    for ax in axs.flat:
        ax.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
