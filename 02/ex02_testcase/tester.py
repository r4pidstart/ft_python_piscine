import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "ex02"))
import load_csv  # type: ignore
import aff_pop  # type: ignore

loaded_df = load_csv.load("ex02_testcase/population_total.csv")
print(loaded_df)

aff_pop.aff_pop(loaded_df, ["France", "South Korea"])

print("----- tc1 invalid dataframe -----")
aff_pop.aff_pop("invalid_dataframe", ["France"])
print()

print("----- tc2 country not found -----")
aff_pop.aff_pop(loaded_df, [
    "France", "42", "42Seoul", "Germany", "Italy", "Italy",
])
print()

print("----- tc3 empty country list -----")
aff_pop.aff_pop(loaded_df, [])
print()
