from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array):
    """
    Inverts the color of the image received.
    """
    res = array.copy()
    res[:, :, 0] = 255 - array[:, :, 0]
    res[:, :, 1] = 255 - array[:, :, 1]
    res[:, :, 2] = 255 - array[:, :, 2]
    plt.rcParams["toolbar"] = "None"
    plt.imshow(res)
    plt.show()


def ft_red(array):
    """
    Extracts the red channel from the image received.
    """
    res = array.copy()
    res[:, :, 0] = array[:, :, 0]
    res[:, :, 1] = 0
    res[:, :, 2] = 0
    plt.rcParams["toolbar"] = "None"
    plt.imshow(res)
    plt.show()


def ft_green(array):
    """
    Extracts the green channel from the image received.
    """
    res = array.copy()
    res[:, :, 0] = 0
    res[:, :, 1] = array[:, :, 1]
    res[:, :, 2] = 0
    plt.rcParams["toolbar"] = "None"
    plt.imshow(res)
    plt.show()


def ft_blue(array):
    """
    Extracts the blue channel from the image received.
    """
    res = array.copy()
    res[:, :, 0] = 0
    res[:, :, 1] = 0
    res[:, :, 2] = array[:, :, 2]
    plt.rcParams["toolbar"] = "None"
    plt.imshow(res)
    plt.show()


def ft_grey(array):
    """
    Converts the image to grayscale by averaging the RGB channels.
    """
    res = np.dot(array[:, :, :3], [1/3, 1/3, 1/3])

    plt.rcParams["toolbar"] = "None"
    plt.imshow(res, cmap="grey")
    plt.show()


def main():
    array = ft_load("../landscape.jpg")

    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
