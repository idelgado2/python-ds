
# Node class for the trie
class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes
        self.children = {}
        # Flag to indicate end of a word
        self.is_end = False


# Trie data structure class
class Trie:
    def __init__(self):
        # Initialize the root node
        self.root = TrieNode()

    def insert(self, word):
        # Insert a word into the trie
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word):
        # Search for a word in the trie
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def starts_with(self, prefix):
        # Check if any word in the trie starts with the given prefix
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

    def __repr__(self):
        # Return a string representation of all words in the trie
        words = []
        self._collect_words(self.root, "", words)
        return f"Trie({words})"

    def _collect_words(self, node, prefix, words):
        # Helper method to collect all words in the trie
        if node.is_end:
            words.append(prefix)
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)

# Example usage
trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("dog")
print(trie)                    # Output: Trie(['cat', 'car', 'dog'])
print(trie.search("cat"))     # Output: True
print(trie.search("can"))     # Output: False
print(trie.starts_with("ca")) # Output: True
print(trie.starts_with("do")) # Output: True
print(trie.starts_with("da")) # Output: False
