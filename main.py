# Source : https://www.programiz.com/dsa/binary-tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):




    def insert(self, data):

        if self.val:

            if data < self.val:

                if self.left is None:

                    self.left = Node(data)

                else:

                    self.left.insert(data)

            elif data > self.val:

                if self.right is None:

                    self.right = Node(data)

                else:

                    self.right.insert(data)
        else:
            self.val = data

    def printTree(self):

        if self.left:
            self.left.printTree()

        print(self.val)

        if self.right:
            self.right.printTree()





    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()


    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')


# Source : https://www.educative.io/answers/how-to-count-the-number-of-nodes-in-a-binary-tree-in-python

def count_nodes(node):

    if node is None:
        return 0
    else:
        return 1 + count_nodes(node.left) + count_nodes(node.right)



root = Node(15)

# Test linear data
for i in range(0, 100):

    root.insert(i)



print(count_nodes(root))


