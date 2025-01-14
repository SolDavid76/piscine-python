from load_csv import load
import matplotlib.pyplot as plt


def strToNumber(lst: list[str]) -> list[float]:
    """
    strToNumber(lst: list[str]) -> list[float]

    This function take one parameter:
    1. list of string using K, M, B
    The function return a list of float converted to usable values
    """
    res = []
    for i in range(len(lst)):
        if lst[i].endswith('B'):
            res.append(float(lst[i][:-1]) * 1e9)
        elif lst[i].endswith('M'):
            res.append(float(lst[i][:-1]) * 1e6)
        elif lst[i].endswith('K'):
            res.append(float(lst[i][:-1]) * 1e3)
        else:
            res.append(float(lst[i]))
    return res


def main():
    data = load("../population_total.csv")

    france_data = data[data["country"] == "France"]
    france_pop = strToNumber(france_data.values[0][1:251])
    belgium_data = data[data["country"] == "Belgium"]
    belgium_pop = strToNumber(belgium_data.values[0][1:251])

    years = france_data.columns[1:251]

    plt.plot(years, france_pop, label="France", color="green")
    plt.plot(years, belgium_pop, label="Belgium", color="blue")
    plt.legend(loc='lower right')
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.xticks(years[::40], rotation=45)
    plt.ylabel("Population")
    plt.yticks([20e6, 40e6, 60e6], ["20M", "40M", "60M"])
    plt.show()


if __name__ == "__main__":
    main()
