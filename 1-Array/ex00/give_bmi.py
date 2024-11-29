def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    give_bmi(height: list[int|float], weight: list[int|float])->list[int|float]

    This function take two parameters:
    1. list of int or float to represent the height
    2. list of int or float to represent the weight
    The function return a list witch each element is (weight / height ** 2)
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("The provided arg are not list")
        if not all(isinstance(x, (int, float)) for x in (height + weight)):
            raise TypeError("The list does not contain only int and float")
        if len(height) != len(weight):
            raise ValueError("The lists have not the same lentght")
        return [w / h ** 2 for h, w in zip(height, weight)]
    except TypeError as error:
        print("TypeError:", error)
    except ValueError as error:
        print("ValueError:", error)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit(bmi: list[int | float], limit: int) -> list[bool]

    This function take two parameters:
    1. list of int or float to represent the bmi
    2. int to represent a limit
    The function return a list of boolean which each element is (bmi > limit)
    """
    try:
        if not isinstance(bmi, list):
            raise TypeError("The provided arg are not list")
        if not all(isinstance(x, (int, float)) for x in bmi):
            raise TypeError("The list does not contain only int and float")
        return [x > limit for x in bmi]
    except TypeError as error:
        print("TypeError:", error)


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
