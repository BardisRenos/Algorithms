# You create the node object
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create the tree structure
class Tree:
    def createNode(self, data):
        return Node(data)

    # Create the function to insert values into the tree
    def insert(self, node, data):

        if node is None:
            return self.createNode(data)
        if data < node.value:
            node.left = self.insert(node.left, data)
        elif data > node.value:
            node.right = self.insert(node.right, data)

        return node

    # This method prints in Pre order morph
    def printPreOrder(self, root):
        if root is not None:
            self.printPreOrder(root.left)
            print(root.value)
            self.printPreOrder(root.right)


if __name__ == '__main__':
    root = None
    tree = Tree()
    root = tree.insert(root, 5)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    tree.printPreOrder(root)