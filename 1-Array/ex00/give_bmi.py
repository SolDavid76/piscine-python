def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    try:
        if len(height) != len(weight):
            raise ValueError("The lists have not the same lentght")
        return [w / h ** 2 for h, w in zip(height, weight)]
    except ValueError as error:
        print("ValueError: ", error)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [x > limit for x in bmi]


if __name__ == "__main__":
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
