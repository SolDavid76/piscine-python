def slice_me(family: list, start: int, end: int) -> list:
    """
    def slice_me(family: list, start: int, end: int) -> list:

    This function take three parameters:
    1. list of array to represent the two dimentions
    2. int to deteremine the start of truncated version of the list
    3. int to deteremine the end of truncated version of the list
    The function return the truncated list with start included but not end
    """
    try:
        if not all(isinstance(x, list) for x in family):
            raise TypeError("The list does not contain only lists")
        if all(len(list) != len(family[0]) for list in family):
            raise ValueError("The lists have not the same size")
        print(f"My shape is : ({len(family)}, {len(family[0])})")
        print(f"My new shape is : ({start% len(family)}, {end % len(family)})")
        return (family[start:end])
    except TypeError as error:
        print("TypeError:", error)
    except ValueError as error:
        print("ValueError:", error)


def main():
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
