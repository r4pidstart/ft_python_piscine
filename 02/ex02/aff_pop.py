import pandas
import matplotlib.pyplot as plt
import seaborn as sns


def convert_to_int(value: str) -> int:
    """Convert string value to integer"""

    if isinstance(value, (int, float)):
        return int(value)
    if not isinstance(value, str):
        return 0

    if value[-1] == 'K' or value[-1] == 'k':
        return int(float(value[:-1]) * 1e3)
    if value[-1] == 'M' or value[-1] == 'm':
        return int(float(value[:-1]) * 1e6)
    if value[-1] == 'B' or value[-1] == 'b':
        return int(float(value[:-1]) * 1e9)
    return int(value)


def aff_pop(dataframe: pandas.DataFrame, country_name: list[str]) -> None:
    """
    Display a graph of the country's population of the given dataframe
    using seaborn
    """

    if not isinstance(dataframe, pandas.DataFrame):
        print("Error: invalid dataframe.")
        return

    if 'country' not in dataframe.columns:
        print("Error: missing columns.")
        return

    try:
        if 'South Korea' not in country_name:
            country_name.append('South Korea')

        country_data = dataframe[dataframe['country'].isin(country_name)]
        if country_data.empty:
            print(f"Error: cannot find country '{country_name}'.")
            return

        country_data = country_data.melt(
            id_vars='country',
            var_name='Year',
            value_name='Population'
        )
        country_data['Year'] = country_data['Year'].astype(int)
        country_data = country_data[
            (1800 <= country_data['Year']) & (country_data['Year'] < 2050)
        ]

        country_data['Population'] = country_data['Population']\
            .map(convert_to_int)

        sns.lineplot(
            data=country_data,
            x="Year",
            y="Population",
            hue='country',
        )

        plt.title("Population projection")
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Error: {e}")
        return
