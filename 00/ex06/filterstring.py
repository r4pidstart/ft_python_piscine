import sys
from ft_filter import ft_filter


def main():
    """program that accepts two arguments: a string(S), and an integer(N).
The program should output a list of words from S \
that have a length greater than N"""

    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    if not sys.argv[2].isdigit():
        print("AssertionError: the arguments are bad")
        return

    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    if [c for c in sys.argv[1] if c in punctuation]:
        print("AssertionError: the arguments are bad")
        return

    whitespace = "\t\n\r\v\f"
    if [c for c in sys.argv[1] if c in whitespace]:
        print("AssertionError: the arguments are bad")
        return

    user_string = sys.argv[1]
    n = int(sys.argv[2])

    words = user_string.split(' ')
    print(ft_filter(lambda x: len(x) > n, words))


if __name__ == "__main__":
    main()
