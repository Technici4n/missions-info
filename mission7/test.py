# Mission 7 - fichier de tests
# Made by Bruno Ploumhans and Victor Poncelet
# Use `python -m unittest discover` to test the code
import unittest
import os
import mission7 as m

EXAMPLE_STRING = """\
While the Congress of the Republic endlessly debates
this alarming chain of events, the Supreme Chancellor has
secretly dispatched two Jedi Knights."""
EXAMPLE_ARRAY = [
    "While the Congress of the Republic endlessly debates\n",
    "this alarming chain of events, the Supreme Chancellor has\n",
    "secretly dispatched two Jedi Knights."
]
EXAMPLE_INDEX = {
    'while': {
        0: 1
    },
    'the': {
        0: 2,
        1: 1
    },
    'congress': {
        0: 1
    },
    'of': {
        0: 1,
        1: 1
    },
    'republic': {
        0: 1
    },
    'endlessly': {
        0: 1
    },
    'debates': {
        0: 1
    },
    'this': {
        1: 1
    },
    'alarming': {
        1: 1
    },
    'chain': {
        1: 1
    },
    'events': {
        1: 1
    },
    'supreme': {
        1: 1
    },
    'chancellor': {
        1: 1
    },
    'has': {
        1: 1
    },
    'secretly': {
        2: 1
    },
    'dispatched': {
        2: 1
    },
    'two': {
        2: 1
    },
    'jedi': {
        2: 1
    },
    'knights': {
        2: 1
    }
}

TEST_FILENAME = 'c7e5fe95e41b3b690fb2c1f14a3699502feeb96a.txt'


class TestProgram(unittest.TestCase):
    def setUp(self):
        with open(TEST_FILENAME, 'w') as f:
            f.write(EXAMPLE_STRING)

    def test_get_words(self):
        # Basic example
        self.assertTrue(
            m.get_words("Turmoil has engulfed the Galactic Republic.") ==
            ["turmoil", "has", "engulfed", "the", "galactic", "republic"])
        # More complicated string with multiple occurrences of the same word and real punctuation
        self.assertTrue(
            m.get_words(
                "I'd like some punctuation for breakfast!!!Hi there I am there..."
            ) == [
                "i", "d", "like", "some", "punctuation", "for", "breakfast",
                "hi", "there", "i", "am", "there"
            ])

    def test_create_index_for_string(self):
        # Sufficiently complex example
        self.assertTrue(
            m.create_index_for_string(EXAMPLE_ARRAY) == EXAMPLE_INDEX)

    def test_get_lines(self):
        # Multiple words at the same time
        self.assertTrue(sorted(m.get_lines(['of', 'the'], EXAMPLE_INDEX)) == [0, 1])
        # Unsuccessful matching
        self.assertTrue(sorted(m.get_lines(['supreme', 'jedi'], EXAMPLE_INDEX)) == [])
        # Non-existing words
        self.assertTrue(
            sorted(m.get_lines(['idontexist', 'neitherdoi'], EXAMPLE_INDEX)) == [])
        # Mixed
        self.assertTrue(sorted(m.get_lines(['i', 'dontexist'], EXAMPLE_INDEX)) == [])

    def test_readfile(self):
        # Simple test
        self.assertTrue(m.readfile(TEST_FILENAME) == EXAMPLE_ARRAY)

    def test_create_index(self):
        # Make sure it also works with files and not just in memory data structures
        self.assertTrue(m.create_index(TEST_FILENAME) == EXAMPLE_INDEX)

    def tearDown(self):
        os.remove(TEST_FILENAME)

if __name__ == '__main__':
    unittest.main()
