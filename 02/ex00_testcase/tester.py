import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "ex00"))
import load_csv  # type: ignore

print(load_csv.load("ex00_testcase/test.csv"))

print("----- tc1 empty path -----")
print(load_csv.load(""))
print()

print("----- tc2 empty file -----")
print(load_csv.load("ex00_testcase/test_empty.csv"))
print()

print("----- tc3 trailing comma -----")
print(load_csv.load("ex00_testcase/test_trailing_comma.csv"))
print()

print("----- tc4 wrong dimension -----")
print(load_csv.load("ex00_testcase/test_wrong_dimension.csv"))
print()
