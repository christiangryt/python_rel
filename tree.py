class node():
    """
    Class to represent nodes in a binary tree

    1 parents and up to 2 children
    """

    # Value of node
    value = ""

    # Parent variable 
    parent = ""

    # List of Children
    children = []

    def __init__(self, value = 0):
        """
        Init new node with a value
        """

        self.value = value

    def attach_child(self, child):
        """
        Input a single node object to attach to this node as child

        No output
        """

        self.children.append(child)
        child.attach_parent(self)

    def attach_parent(self, parent):
        """
        Input node object to become parent to this node

        No output
        """

        self.parent = parent

n1 = node(5)
n2 = node(6)

print(n2.parent)

n1.attach_child(n2)

print (n2.parent)