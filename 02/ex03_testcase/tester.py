import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "ex03"))
import load_csv  # type: ignore
import projection_life  # type: ignore

loaded_df_income = load_csv.load(
    "ex03_testcase/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
)
loaded_df_life = load_csv.load("ex03_testcase/life_expectancy_years.csv")
print(loaded_df_income)
print(loaded_df_life)

projection_life.projection(loaded_df_life, loaded_df_income, 1900)


print("----- tc1 invalid dataframe -----")
loaded_invalid_dataframe = load_csv.load("ex00_testcase/test_empty.csv")
print(projection_life.projection(loaded_invalid_dataframe, loaded_df_income))

print("----- tc2 invalid dataframe -----")
loaded_invalid_dataframe = load_csv.load("ex03_testcase/test_no_1900.csv")
print(projection_life.projection(loaded_invalid_dataframe, loaded_df_income))
