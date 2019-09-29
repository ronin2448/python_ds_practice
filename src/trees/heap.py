class MinHeap():
    def __init__(self):
        self.root = None
        self.next_available_parent = self.root

    def add(self, value):
        new_node = self.Node(value)
        available_parent = self.root
        while available_parent:
            if not available_parent.left:
                available_parent.left = new_node
            elif not available_parent.right:
                available_parent.right = new_node
            is_complete_left = self.is_complete(available_parent.left)
            is_complete_right = self.is_complete(available_parent.right)
            if is_complete_left:
                if is_complete_right:
                    available_parent = available_parent.left
                else:
                    available_parent = available_parent.right
            available_parent = available_parent.left
        self._heapify()

    def _is_complete(self, root_node):
        if root_node is None:
            return False
        dfs_stack = list()
        while len(dfs_stack) > 0:





    class Node():
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

if __name__ == "__main__":
    min_heap = MinHeap()


      1
   2     3
  5 6
