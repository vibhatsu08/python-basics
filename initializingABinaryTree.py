# Python program to initialise a binary tree.
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def get_val(self):
        return self.key
    
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    print(root.left.get_val())
    
if __name__ == "__main__":
    main()