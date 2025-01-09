import sys


def main():
    """program that accepts two arguments: a string(S), and an integer(N).
The program should output a list of words from S \
that have a length greater than N"""

    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ' ': '/',
        }

    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    user_string = sys.argv[1].upper()

    result = ""
    for c in user_string:
        if c in MORSE_CODE_DICT:
            result = result + MORSE_CODE_DICT[c] + ' '
        else:
            print("AssertionError: the arguments are bad")
            return

    print(result)


if __name__ == "__main__":
    main()
