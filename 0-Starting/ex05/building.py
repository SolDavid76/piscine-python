import sys


def analyze_text(arg: str):
    """
    analyze_text(string)

    Print the following information:
    1.The number of characters in the string
    2.The number of upper case letters
    3.The number of lower case letters
    4.The number of ponctuation marks
    5.The number of spaces
    6.The number of digits
    """

    dict = {"upper": 0, "lower": 0, "punctuation": 0, "spaces": 0, "digits": 0}

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


def main():
    if len(sys.argv) == 2:
        analyze_text(sys.argv[1])
    elif len(sys.argv) == 1:
        print("What us the text to count?")
        analyze_text(sys.stdin.readline())
    else:
        print("AssertionError: more than one argument is provided")


if __name__ == "__main__":
    main()
