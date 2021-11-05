"""
A trie (prefix tree) is used to hold words, has very fast lookup.

See examples for word_search
"""
import collections


class Trie(object):
    """Prefix tree class for iterables/words."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert word into the Trie"""
        node = self.root
        for char in word:
            node = node.children[char]
        node.value = word

    def search(self, word):
        """Return True if word is found in the trie"""
        node = self.root
        for w in word:
            node = node.children.get(w, None)
            if node is None:
                return False
        return node.is_word()

    def match_prefix(self, prefix):
        """Return a list of all matching words to prefix"""
        node = self.root
        for w in prefix:
            node = node.children.get(w, None)
            if node is None:
                return []
        words = []

        node.find_child_words(words)

        return words

    def __str__(self):
        print(
            "Trie with children {}".format(self.root.children)
        )


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.value = None

    def is_word(self):
        return self.value is not None

    def find_child_words(self, in_words):
        for val in self.children.values():
            if val.is_word():
                in_words.append(val.value)
            else:
                val.find_child_words(in_words)

    def __str__(self):
        print(
            "TrieNode with value {} and children {}".format(self.value, self.children)
        )


if __name__ == "__main__":

    main_trie = Trie()

    main_words = [
        "apple",
        "astrolabe",
        "banana",
        "astronomer",
        "astronaut",
        "apparatus",
        "zeal",
        "archer",
        "art",
        "tart",
        [1, 2, 3, 4]
    ]
    for w in main_words:
        main_trie.insert(w)

    print(main_trie.search("apple"))
    print(main_trie.match_prefix("astro"))
    print(main_trie.match_prefix([1, 2]))
