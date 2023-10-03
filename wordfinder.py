"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random() in ["aardvark", "aardwolf", "aaron"]
    True

    >>> wf.random() in ["aardvark", "aardwolf", "aaron"]
    True

    >>> wf.random() in ["aardvark", "aardwolf", "aaron"]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex_words.txt")
    235886 words read

    >>> swf.random() in ["aardvark", "aardwolf", "aaron"]
    True

    >>> swf.random() in ["aardvark", "aardwolf", "aaron"]
    True

    >>> swf.random() in ["aardvark", "aardwolf", "aaron"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]