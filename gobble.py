import os
import sys
import json
import argparse
import secrets
import string

location = os.path.dirname(os.path.abspath(__file__))

WORDLIST = json.load(open(f'{location}/diceware.json', 'rt'))
CHARACTERS = [*string.ascii_letters, *string.digits]
MIN_GIBBERISH = 12
MIN_LENGTH = 25
SIDES = 6
ROLLS = 5


def diceware(number):
    """Generate a list of <number> words."""
    rand = secrets.SystemRandom()
    words = []
    for i in range(number):
        roll = []
        for j in range(ROLLS):
            roll.append(rand.randint(1, SIDES))
        words.append(WORDLIST[''.join(map(str, roll))])
    return words


def gobbledygook(length, charset):
    """Generate a password of <length> random characters from set of
    <characters>.
    """
    password = []
    rand = secrets.SystemRandom()
    for i in range(length):
        password.append(rand.choice(charset))
    return ''.join(password)


def main():
    """The main program."""
    parser = argparse.ArgumentParser(
        description="""Generate passwords secure from the "It's just a bunch of
        gobbledygook" social engineering hack. For details see
        https://news.ycombinator.com/item?id=19051562
        """)

    parser.add_argument('-m', '--min', action='store', type=int, default=25,
                        help="The minimum length of the password. Defaults to "
                        "25 and cannot be set lower than 25 To limit the "
                        "length, use -n.")
    parser.add_argument('-n', '--max', action='store', type=int, help="The "
                        "maximum length of the password, defaults to no limit.")
    parser.add_argument('--nosymbols', action='store_true',
                        help="Disable all symbols.")
    parser.add_argument('-y', '--symbols', action='store', type=str,
                        default=string.punctuation, help="A string consisting "
                        "of the allowable special symbols. Defaults to "
                        "Python's string.punctuation.")
    parser.add_argument('-w', '--words', action='store', type=int, default=1,
                        help="The number of words to use, defaults to 1. "
                        "(NOTE: if set, and the character-length of the "
                        "concatenated words exceeds the chosen length of the "
                        "-l, the password will be truncated.")
    parser.add_argument('-s', '--separator', action='store', type=str,
                        default='_', help="The separator to be used for the "
                        "diceware words. Default is _. NOTE: this can be an "
                        "arbitrary length separator but will abide by length "
                        "rules.")

    args = parser.parse_args()


    words = diceware(args.words)

    # We want the passphrase to end with the separator so the words stand out
    # from the gobbledygook.
    passphrase = f"{args.separator.join(words)}{args.separator}"

    if args.max and args.min > args.max:
        args.min = args.max
    elif args.min < MIN_LENGTH:
        args.min=MIN_LENGTH

    dice = diceware(args.words)
    words = (args.separator.join(dice) + args.separator if not args.nosymbols
             and args.separator in args.symbols else ''.join(dice))

    if args.max and len(words) > args.max:
        parser.error(f"The generated words {words} are longer than your "
        "max length. Either set a higher max or ask for less words.")

    if args.max:
        padding = args.max - len(words)
    else:
        diff = args.min - len(words)
        padding = diff if diff > MIN_GIBBERISH else MIN_GIBBERISH

    charset = [*CHARACTERS] if args.nosymbols else [*CHARACTERS, *args.symbols]
    gibberish = gobbledygook(padding, charset)

    final = f"{words}{gibberish}"
    print("The password is: ")
    print(final)


if __name__ == '__main__':
    main()
