import sys
from ft_filter import ft_filter


def main():
    """
    The program take only 2 arguments
    1. string
    2. int

    Print a list of words that are longer than the 2nd parameter
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError()

        text = sys.argv[1]
        n = int(sys.argv[2])

        if not isinstance(text, str) or not isinstance(n, int):
            raise AssertionError()

        print(list(ft_filter(lambda word: len(word) > n, text.split())))
    except AssertionError:
        print("AssertionError: the arguments are bad")
    except ValueError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
