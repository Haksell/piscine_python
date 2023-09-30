from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Draws a graph of life expectancy in France from 1800 to 2100."""
    df = load("../data/life_expectancy_years.csv")
    df = df[df["country"] == "France"]
    df = df.set_index("country")
    df = df.transpose()
    df.plot(figsize=(6, 5), legend=False)
    plt.title("France life expectancy projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
