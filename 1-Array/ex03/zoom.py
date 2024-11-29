from load_image import ft_load
import matplotlib.pyplot as plt
import os


def main():
    try:
        print("A")
        if not os.path.exists("../animal.jpeg"):
            raise AssertionError("File not found")
        img = ft_load("../animal.jpeg")
        if img is None:
            raise AssertionError("Failed to load image")
        plt.imshow(img)
        plt.axis("off")
        plt.show()
    except AssertionError as error:
        print("AssertionError:", error)

if __name__ == "__main__":
    main()
