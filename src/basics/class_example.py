class tree():
    def __init__(self):
        self.has_leaves = True

    def grow(self):
        print("Growing")


if __name__ == "__main__":
    my_tree = tree()
    my_tree.grow()