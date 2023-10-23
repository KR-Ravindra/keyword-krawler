import hashlib

# Rabin-Karp Algorithm
def rabin_karp(text, keyword):
    keyword_hash = hashlib.sha256(keyword.encode()).hexdigest()
    keyword_len = len(keyword)
    matches = []

    for i in range(len(text) - keyword_len + 1):
        substr = text[i:i + keyword_len]
        substr_hash = hashlib.sha256(substr.encode()).hexdigest()
        if substr_hash == keyword_hash:
            matches.append(substr)

    return matches

# Suffix Tree
class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = {}
        for i in range(len(text)):
            self.add_suffix(text[i:])

    def add_suffix(self, suffix):
        node = self.root
        for char in suffix:
            if char not in node:
                node[char] = {}
            node = node[char]

    def search(self, keyword):
        node = self.root
        for char in keyword:
            if char not in node:
                return False
            node = node[char]
        return True

# Suffix Array
class SuffixArray:
    def __init__(self, text):
        self.text = text
        self.suffixes = sorted(range(len(text)), key=lambda i: text[i:])

    def search(self, keyword):
        low, high = 0, len(self.text)
        while low <= high:
            mid = (low + high) // 2
            suffix_idx = self.suffixes[mid]
            suffix = self.text[suffix_idx:]
            if keyword == suffix[:len(keyword)]:
                return True
            elif keyword < suffix[:len(keyword)]:
                high = mid - 1
            else:
                low = mid + 1
        return False

# Naive String Matching
def naive_string_matching(text, keyword):
    matches = []
    text_len = len(text)
    keyword_len = len(keyword)

    for i in range(text_len - keyword_len + 1):
        if text[i:i + keyword_len] == keyword:
            matches.append(text[i:i + keyword_len])

    return matches

# Knuth-Morris-Pratt (KMP) Algorithm
def kmp_string_matching(text, keyword):
    prefix = [0] * len(keyword)
    matches = []
    k = 0

    for i in range(1, len(keyword)):
        while k > 0 and keyword[k] != keyword[i]:
            k = prefix[k - 1]
        if keyword[k] == keyword[i]:
            k += 1
        prefix[i] = k

    k = 0
    for i in range(len(text)):
        while k > 0 and keyword[k] != text[i]:
            k = prefix[k - 1]
        if keyword[k] == text[i]:
            k += 1
        if k == len(keyword):
            matches.append(text[i - k + 1:i + 1])
            k = prefix[k - 1]

    return matches
