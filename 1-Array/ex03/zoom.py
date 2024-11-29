from load_image import ft_load
import os


def main():
    try:
        if not os.path.exists("../animal.jpeg"):
            raise AssertionError("File not found")
        img = ft_load("../animal.jpeg")
        if img is None:
            raise AssertionError("Failed to load image")
        print
    except AssertionError as error:
        print("AssertionError:", error)

if __name__ == "__main__":
    main()
