from load_csv import load
import matplotlib.pyplot as plt


def main():
    data = load("../life_expectancy_years.csv")
    france_data = data[data["country"] == "France"]
    years = france_data.columns[1:]
    life_expetancy = france_data.values[0][1:]
    plt.plot(years, life_expetancy, label="France")
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.xticks(years[::40], rotation=45)
    plt.ylabel("Life expectancy")
    plt.yticks(range(30, 100, 10))
    plt.show()


if __name__ == "__main__":
    main()
