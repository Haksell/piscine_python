from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def parse_pop(x):
    """Parse population symbols."""
    match x[-1]:
        case "K":
            return float(x[:-1]) * 1e3
        case "M":
            return float(x[:-1]) * 1e6
        case "B":
            return float(x[:-1]) * 1e9
        case _:
            return float(x)


def aff_pop():
    """Draws a graph of population projections from  in France from 1800 to 2050."""
    df = load("../data/population_total.csv")
    df = df[(df["country"] == "France") | (df["country"] == "Mexico")]
    df = df.set_index("country")
    df = df.applymap(parse_pop)
    df = df.loc[:, "1800":"2050"]
    df = df.transpose()
    print(df)
    _, ax = plt.subplots(figsize=(6, 5))
    df.plot(ax=ax)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f"{x/1e6:.0f}M"))
    ax.set_yticks([i * 2e7 for i in range(9)])
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.show()


if __name__ == "__main__":
    aff_pop()
