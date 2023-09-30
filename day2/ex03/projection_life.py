import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Make a scatter plot of GDP vs life expectancy for 1900."""
    income_data = load(
        "../data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
    )
    income_data = income_data.set_index("country")
    life_expectancy_data = load("../data/life_expectancy_years.csv")
    life_expectancy_data = life_expectancy_data.set_index("country")

    merged_data = pd.merge(
        income_data,
        life_expectancy_data,
        on="country",
        suffixes=("_income", "_life_expectancy"),
    )
    data_1900 = merged_data[["1900_income", "1900_life_expectancy"]].dropna()

    plt.figure(figsize=(6, 5))
    plt.scatter(data_1900["1900_income"], data_1900["1900_life_expectancy"])
    plt.title("1900")
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")

    log_gdp = np.log(data_1900["1900_income"])
    m, b = np.polyfit(log_gdp, data_1900["1900_life_expectancy"], 1)
    plt.plot(data_1900["1900_income"], m * log_gdp + b, color="red")

    plt.show()


if __name__ == "__main__":
    main()
