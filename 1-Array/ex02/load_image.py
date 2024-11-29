import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> list:
    """
    ft_load(path: str) -> list

    This function take one parameter:
    1. string to determine the path of image to load
    The function return a list[list[list[int]]] wtich represent all the pixels
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("File not found")
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported")
        img = Image.open(path)
        print(f"The shape of image is: {img.size[1], img.size[0], img.layers}")
        return np.array(img)
    except AssertionError as error:
        print("AssertionError:", error)


def main():
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
