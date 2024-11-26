import sys


def encode_morse(text: str) -> str:
    morse = {
        ' ': '/',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----'
    }
    res = []

    for i, char in enumerate(text):
        if char in morse:
            res.append(morse[char])
        else:
            raise AssertionError()
    return ' '.join(res)


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError()

        print(encode_morse(sys.argv[1].upper()))

    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
