# Source : https://www.geeksforgeeks.org/binarytree-module-in-python/

from binarytree import build
import random

nodes = []

for i in range(0, 20):

    nodes.append(i)

binary_tree = build(nodes)
print(binary_tree)

"""
for i in range(random.randint(0, 100)):
    
    nodes.append(i)

binary_tree = build(nodes)
print(binary_tree)
    """
