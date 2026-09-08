"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Each node stores one value and begins with no children.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # The root starts as None because the tree is empty.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # The recursive helper returns the updated root.
        # Smaller values go left and larger values go right,
        # which keeps the BST organized for efficient searching.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # If an empty position is found, create a new node there.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored in this implementation.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # A BST can reduce the search space at each step because
        # values smaller than a node are on the left and larger
        # values are on the right. This can be faster than checking
        # every item one by one in a linear structure.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # If the search reaches an empty position, the value is not present.
        if node is None:
            return False

        # If the current node matches, the value was found.
        if value == node.value:
            return True

        # Search only the side where the value could exist.
        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        if node is not None:
            # Visit smaller values first by traversing the left subtree.
            self._inorder_recursive(node.left, values)

            # Visit the current node.
            values.append(node.value)

            # Visit larger values last by traversing the right subtree.
            self._inorder_recursive(node.right, values)

            # Because BST values are arranged as left < node < right,
            # in-order traversal produces the values in sorted order.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Create the BST.
    tree = BST()

    # These values create both left and right subtrees.
    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        tree.insert(value)

    # BST searching can reduce the remaining search space at each step
    # because comparisons determine whether to continue left or right.
    print("Values inserted:", values)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # In-order traversal visits left, current node, then right.
    # Since smaller values are stored on the left and larger values
    # are stored on the right, the final result is sorted.
    traversal = tree.inorder()
    print("In-order traversal:", traversal)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Existing values should return True.
    print("Search for 40:", tree.search(40))
    print("Search for 70:", tree.search(70))

    # Missing values should return False.
    print("Search for 25:", tree.search(25))
    print("Search for 90:", tree.search(90))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Create an empty BST.
    empty_tree = BST()

    # Traversing an empty tree returns an empty list.
    print("Empty tree traversal:", empty_tree.inorder())

    # Searching an empty tree returns False because there are no nodes.
    print("Search empty tree for 50:", empty_tree.search(50))


if __name__ == "__main__":
    main()
