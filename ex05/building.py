import sys


def main():
    dict = {"upper": 0, "lower": 0, "punctuation": 0, "spaces": 0, "digits": 0}

    if len(sys.argv) == 2:
        arg = sys.argv[1]
    elif len(sys.argv) == 1:
        print("What us the text to count?")
        arg = sys.stdin.readline()
    else:
        print("AssertionError: more than one argument is provided")
        return 1

    for i, char in enumerate(arg):
        if char.isupper():
            dict["upper"] += 1
        elif char.islower():
            dict["lower"] += 1
        elif char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            dict["punctuation"] += 1
        elif char.isspace():
            dict["spaces"] += 1
        elif char.isnumeric():
            dict["digits"] += 1

    print(f"The text contains {len(arg)} characters:")
    print(f"{dict['upper']} upper letters")
    print(f"{dict['lower']} lower letters")
    print(f"{dict['punctuation']} punctuation marks")
    print(f"{dict['spaces']} spaces")
    print(f"{dict['digits']} digits")
    return 0


if __name__ == "__main__":
    main()
