import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os


def main():
    """
    This function opens '../animal.jpeg',
    crops it to 400x400 pixels,
    and rotates it 90 degrees to the left.
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
        grey_array = np.asarray(grey_img)
        transposed_array = [
            [grey_array[j][i] for j in range(len(grey_array))]
            for i in range(len(grey_array[0]))
        ]

        print(f"The shape of image is: {grey_img.size}")
        print(np.asarray(img))
        print(f"New shape after Transpose: {grey_img.size}")
        print(np.array(transposed_array))

        plt.rcParams["toolbar"] = "None"
        plt.imshow(transposed_array, cmap="grey")
        plt.show()
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
