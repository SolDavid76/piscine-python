from load_csv import load


def main():
    test = load("../life_expectancy_years.csv")
    print(test[test["country"] == "France"])

if __name__ == "__main__":
    main()
