class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            node.parent = self

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None

    @parent.setter
    def parent(self, node):
        if self._parent is node:
            return
        if self._parent is not None:
            self._parent.remove_child(self)
        self._parent = node
        if node is not None:
            node.add_child(self)

    def depth_search(self, value):
        if self._value == value:
            return self
        for node in self._children:
            child = node.depth_search(value)
            if child:
                return child
        return None

    def breadth_search(self, value):
        search = [self]

        while search:
            node = search.pop(0)
            if node._value == value:
                return node
            search.extend(node._children)

        return None


# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node3.parent = node1
# node3.parent = node2

# print(node1.children)
# print(node2.children)
