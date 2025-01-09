import sys


def main():
    """takes a single string argument and displays the sums of its upper-case \
characters, lower-casecharacters, punctuation characters, digits and spaces."""

    if not (len(sys.argv) < 3):
        print("AssertionError: more than one argument is provided")
        return

    user_string = ""
    if len(sys.argv) == 2:
        user_string = sys.argv[1]
    else:
        user_string = input("What is the text to count?\n")

    print(f"The text contains {len(user_string)} characters:")
    print(f"{sum(map(str.isupper, user_string))} upper letters")
    print(f"{sum(map(str.islower, user_string))} lower letters")
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    print(f"{sum(1 for c in user_string if c in punctuation)} "
          "punctuation marks")
    print(f"{sum(map(str.isspace, user_string))} spaces")
    print(f"{sum(map(str.isdigit, user_string))} digits")


if __name__ == "__main__":
    main()
