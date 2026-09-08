# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduced Binary Search Trees (BSTs) and recursive tree operations.

For this assignment, I created a Binary Search Tree in Python. The program demonstrated recursive insertion, recursive searching, in-order traversal, and edge-case handling.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Built a BST.
2. Inserted multiple values.
3. Demonstrated in-order traversal.
4. Tested searching.
5. Demonstrated edge cases.
6. Created a real-world BST example.

## Implementation

I created a Binary Search Tree using `Node` and `BST` classes. Each node stored a value and references to its left and right children.

I inserted the values:

50, 30, 70, 20, 40, 60, 80

Values smaller than the current node were inserted into the left subtree, while larger values were inserted into the right subtree. This created a balanced tree that could reduce the search space during each comparison.

The tree had the following structure:

        50
       /  \
     30    70
    / \    / \
   20 40  60 80

## In-Order Traversal

I used recursive in-order traversal to visit the left subtree, the current node, and then the right subtree.

The resulting traversal was:

20, 30, 40, 50, 60, 70, 80

The output was sorted because a Binary Search Tree stores smaller values to the left and larger values to the right.

## Search Testing

I searched for values that existed and values that were not present in the tree.

- Searching for 40 returned `True`.
- Searching for 70 returned `True`.
- Searching for 25 returned `False`.
- Searching for 90 returned `False`.

The BST used comparisons to determine whether to continue searching the left or right subtree instead of checking every value.

## Edge Cases

I tested an empty Binary Search Tree as an edge case. Performing an in-order traversal on the empty tree returned an empty list.

Searching the empty tree for 50 returned `False` because the tree contained no nodes.

## Real-World Application

A Binary Search Tree could be used to organize employee records by employee ID. Each employee ID could be stored as a node, allowing the program to decide whether to search the left or right subtree based on the requested ID.

A reasonably balanced BST could make searching more efficient because each comparison reduces the remaining search space. However, if values were inserted in sorted or sequential order, the BST could become unbalanced and behave more like a linked list, making searches less efficient.

## Discussion Board Reflection

I learned how Binary Search Trees organize data using relationships between nodes and how recursion can be used for insertion, searching, and traversal. I also learned that values smaller than a node are placed on the left while larger values are placed on the right.

The recursive methods were the most challenging part because I had to understand how each method continued calling itself until it reached a base case. Working through the insertion and search methods helped me understand how recursion moves through different branches of a tree.

BSTs can improve search efficiency because they use the ordering of their values to determine which side of the tree should be searched. In a balanced BST, this can reduce the search space with each comparison instead of checking every element as a linear search might. However, insertion order is important. If values are inserted in sequential order, the tree can become unbalanced and resemble a linked list, reducing the performance advantage of the BST.
