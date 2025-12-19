import pandas
import matplotlib.pyplot as plt
import seaborn as sns


def projection(
        life_expectancy: pandas.DataFrame,
        income_per_person: pandas.DataFrame,
        year: int = 1900,
        ) -> None:
    """
        Project the relationship of the life expectancy and
        income per person in the given year using seaborn
    """

    if not isinstance(life_expectancy, pandas.DataFrame):
        print("Error: invalid dataframe.")
        return
    if not isinstance(income_per_person, pandas.DataFrame):
        print("Error: invalid dataframe.")
        return

    try:
        life_expectancy = life_expectancy.melt(
            id_vars='country',
            var_name='Year',
            value_name='Life expectancy'
        )

        income_per_person = income_per_person.melt(
            id_vars='country',
            var_name='Year',
            value_name='Gross domestic product'
        )

        life_expectancy = life_expectancy[
            life_expectancy['Year'] == str(year)
        ]  # type: ignore
        income_per_person = income_per_person[
            income_per_person['Year'] == str(year)
        ]  # type: ignore

        life_expectancy = life_expectancy.drop('Year', axis=1)
        income_per_person = income_per_person.drop('Year', axis=1)

        merged_data = pandas.merge(
            life_expectancy,
            income_per_person,
            on='country',
        )

        sns.scatterplot(
            data=merged_data,
            y="Life expectancy",
            x="Gross domestic product",
        )
        plt.title(str(year))
        plt.show()

    except Exception as e:
        print(f"Error: {e}")
        return
