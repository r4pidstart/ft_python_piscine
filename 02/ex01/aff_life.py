import pandas
import matplotlib.pyplot as plt
import seaborn as sns


def aff_life(dataframe: pandas.DataFrame, country_name: str = "South Korea")\
        -> None:
    """
    Display a graph of the country's life expenctancy of the given dataframe
    using seaborn
    """

    if not isinstance(dataframe, pandas.DataFrame):
        print("Error: invalid dataframe.")
        return

    if 'country' not in dataframe.columns:
        print("Error: missing columns.")
        return

    try:
        country_data = dataframe[dataframe['country'] == country_name]

        country_data = country_data.drop('country', axis=1).T
        country_data.columns = ['Life expectancy']
        country_data.index.name = 'Year'
        country_data = country_data.reset_index()
        country_data['Year'] = country_data['Year'].astype(int)

        sns.lineplot(
            data=country_data,
            x="Year",
            y="Life expectancy",
        )

        plt.title(f"{country_name} Life expectancy projection")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
