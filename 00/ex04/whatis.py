import sys


if len(sys.argv) == 1:
    sys.exit()

# assert len(sys.argv) < 3, "more than one argument is provided"
if not (len(sys.argv) < 3):
    print("AssertionError: more than one argument is provided")
    sys.exit()

# assert sys.argv[1].isdigit(), "argument is not an integer"
if not sys.argv[1].isdigit():
    print("AssertionError: argument is not an integer")
    sys.exit()

if int(sys.argv[1]) % 2 == 0:
    print("I'm even.")
else:
    print("I'm odd.")
