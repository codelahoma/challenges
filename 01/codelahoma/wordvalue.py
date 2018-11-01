from collections import Counter

from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        return [line.strip() for line in f if line.strip().isalpha()]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    counter = Counter(word.upper())
    return sum([v * LETTER_SCORES[k] for k, v in counter.items()])


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if words is not None:
        return max(words, key=calc_word_value)
    else:
        return max(load_words(), key=calc_word_value)


if __name__ == "__main__":
    assert (calc_word_value('junk') == 15)
    assert (calc_word_value('zoo') == 12)

    assert (max_word_value(['junk', 'zoo']) == 'junk')
    assert (max_word_value() == 'benzalphenylhydrazone')
