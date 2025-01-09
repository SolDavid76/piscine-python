from load_csv import load
import matplotlib.pyplot as plt


def main():
    data = load("../population_total.csv")
    france_data = data[data["country"] == "France"]
    years = france_data.columns[1:]
    total_pop = france_data.values[0][1:]
    plt.plot(years, total_pop, label="France")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.xticks(years[::40], rotation=45)
    plt.ylabel("Population")
    plt.yticks(range(30, 100, 10))
    plt.show()


if __name__ == "__main__":
    main()
