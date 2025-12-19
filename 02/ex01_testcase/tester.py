import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "ex01"))
import load_csv  # type: ignore
import aff_life  # type: ignore

loaded_df = load_csv.load("ex01_testcase/life_expectancy_years.csv")
print(loaded_df)

aff_life.aff_life(loaded_df, "France")
aff_life.aff_life(loaded_df, "South Korea")

print("----- tc1 invalid dataframe -----")
aff_life.aff_life("invalid_dataframe", "France")
print()

print("----- tc2 country not found -----")
aff_life.aff_life(loaded_df, "42")
print()

print("----- tc3 nan -----")
aff_life.aff_life(loaded_df, "Andorra")
