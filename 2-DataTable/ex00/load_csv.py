import pandas
import os


def load(path: str) -> pandas.DataFrame:
    try:
        if not os.path.exists(path):
            raise AssertionError(f"File not found({path})")
        if not path.lower().endswith(".csv"):
            raise AssertionError("Only CSV formats are supported")
        return pandas.read_csv(path)
    except AssertionError as error:
        print("AssersionError:", error)


def main():
    print(load("../life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
