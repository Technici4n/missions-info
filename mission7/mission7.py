# Mission 7 - fichier exécutable
# Made by Bruno Ploumhans and Victor Poncelet
import os
import string
import sys


def readfile(filename):
    """Read file `filename` and output an array of lines.

    May throw OSError. Look up the documentation about `open` for more information."""
    with open(filename, 'r') as f:
        return f.readlines()


def get_words(line):
    """Remove punctuation from `line`, lowercase it and split it."""
    return ''.join([c if c not in string.punctuation else ' '
                    for c in line]).lower().split()


def create_index_for_string(text):
    """Create an index for line array `text`.

    An index maps every word to a dictionary containing the number of occurences of the string for every line in which it appears. For example, the index for `["a b b", "a"]` is `{"a": {0: 1, 1: 1}, "b": {0: 2}}`."""
    index = {}
    for i, line in enumerate(text):
        for w in get_words(line):
            index[w] = index.get(w, {})
            index[w][i] = (index[w].get(i) or 0) + 1
    return index


def create_index(filename):
    """Create an index for file `filename`.

    Look up the documentation about `create_index_for_string` for more information about indices.
    May throw OSError. Look up the documentation about `open` for more information."""
    return create_index_for_string(readfile(filename))


def get_lines(words, index):
    """Get all lines containing the words in `words` using the index `index`.

    More precisely, returns an (unsorted) list of the indices of all the lines containing all the words in `words`.
    Look up the documentation about `create_index_for_string` for more information about indices.
    """

    def lines_with_word(w):
        return set({}) if w not in index else {i for i in index[w]}

    lines = lines_with_word(words[0])
    for w in words[1:]:
        lines = lines.intersection(lines_with_word(w))
    return list(lines)


def main_loop(input_stream, output_stream):
    """Start a main loop using custom streams."""

    def pr(*text, end='\n'):
        print(*text, end=end, file=output_stream, flush=True)

    def prompt(text):
        ipt = input('(%s) > ' % text)
        if ipt == '\\q':
            raise EOFError
        return ipt

    def somehow_get_index():
        pr('Please type the name of the file you want to search in.')
        while True:
            try:
                filename = prompt('file name')
                return create_index(filename)
            except OSError:
                pr("That file doesn't exist, you silly!")

    def prompt_for_words():
        return input('(word list) > ')

    try:
        pr('Welcome to the file searcher.')
        pr("Type \\q to exit the program at any time.")
        index = somehow_get_index()
        pr("Great! Now you can type words separated by spaces to search for line matching all of them."
           )
        while True:
            line = prompt('word list')
            words = line.lower().split()
            if len(words) == 0:
                pr("Wait! You forgot to type those words, didn't you?")
                continue
            search_result = get_lines(words, index)
            if len(search_result) == 0:
                pr("No matching line found. Does the word you asked for even exist?"
                   )
            else:
                pr("Matching lines: %s." % ', '.join(
                    [str(x) for x in sorted(search_result)]))
    except EOFError:
        pass
    pr('Bye, have a great time!')


def main():
    """Start a main loop using standard streams."""
    main_loop(sys.stdin, sys.stdout)


if __name__ == '__main__':
    main()
