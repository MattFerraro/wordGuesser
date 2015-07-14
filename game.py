import random
import argparse


def main(reference_word=None, full_auto=False):
    # First open up a dictionary and read all the words
    words = []
    WORD_LENGTH = 5
    with open("/usr/share/dict/words", "r") as f:
        words = f.readlines()

    # Chop out words that are the wrong length
    words = [x.strip() for x in words if len(x.strip()) == WORD_LENGTH]

    while True:
        print "Possible candidates: {}".format(len(words))
        next_guess = random.choice(words)

        if reference_word:
            print "Guessing: ", next_guess
            shared = find_shared(next_guess, reference_word)
        else:
            shared = get_shared(next_guess)

        guess_set = set(next_guess.lower())

        words = [
            x for x in words if len(
                guess_set.intersection(set(x.lower()))) == shared]
        # reject_words = [
        #     x for x in words if len(
        #         guess_set.intersection(set(x.lower()))) != shared]

        if shared == 5:
            print "I got it! Your word is one of these:", words
            break
        elif next_guess.strip() in words:
            words.remove(next_guess.strip())


def find_shared(input_word, reference_word):
    a = set(input_word.lower())
    b = set(reference_word.lower())
    return len(a.intersection(b))


def get_shared(input_word):
    while True:
        shared = raw_input(
            "How many shared letters with {}? ".format(input_word.upper()))

        try:
            shared = int(shared)
        except:
            print "Invalid input!"
            continue

        if shared < 0 or shared > len(input_word):
            print "Invalid input!"
            continue

        return shared


if __name__ == '__main__':
    aparser = argparse.ArgumentParser(
        description="Plays that one word game")
    aparser.add_argument(
        "--reference_word",
        "-r",
        help="The reference word, just to see how it plays")
    aparser.add_argument(
        "--full_auto",
        "-f",
        help="Run in full auto mode",
        action="store_true")
    args = aparser.parse_args()

    main(args.reference_word, args.full_auto)
