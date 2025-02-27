import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os


def main():
    """
    This function opens '../animal.jpeg',
    crops it to 400x400 pixels.
    """
    try:
        path = "../animal.jpeg"
        if not os.path.exists(path):
            raise AssertionError(f"File not found ({path})")
        img = Image.open(path)
        if img is None:
            raise AssertionError("Failed to load image")

        zoomed_img = img.crop((400, 100, 800, 500))
        grey_img = zoomed_img.convert("L")
        print(zoomed_img.convert.__doc__)
        print(f"The shape of image is: {img.size[1], img.size[0], img.layers}")
        print(np.asarray(img))
        print(f"New chape after slicing: {grey_img.size}")
        print(np.asarray(grey_img))

        plt.rcParams["toolbar"] = "None"
        plt.imshow(grey_img, cmap="grey")
        plt.show()
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
