class BinaryTree:
    #Time ans Space Complexity is O(1)
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
