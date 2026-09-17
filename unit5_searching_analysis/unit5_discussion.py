"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Linear search checks each element one at a time from beginning to end.
    # In the worst case, every element must be checked, giving O(n) complexity.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # Return -1 if the target was not found.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    # Set the beginning and end of the search range.
    low = 0
    high = len(lst) - 1

    while low <= high:
        # Find the middle position of the current search range.
        middle = (low + high) // 2

        if lst[middle] == target:
            return middle

        # If the target is greater than the middle value,
        # eliminate the entire left half of the search space.
        elif target > lst[middle]:
            low = middle + 1

        # Otherwise, eliminate the entire right half.
        else:
            high = middle - 1

        # Each iteration removes about half of the remaining values,
        # which gives binary search O(log n) time complexity.

    # Return -1 if the target was not found.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # Create a small sorted list of student scores.
    small_scores = [55, 67, 72, 81, 90, 95]

    # 81 exists in the list at index 3.
    existing_score = 81

    # 85 does not exist, so both algorithms should return -1.
    missing_score = 85

    print("Small dataset:", small_scores)

    print("\nSearching for existing score:", existing_score)
    print("Linear search result:",
          linear_search(small_scores, existing_score))
    print("Binary search result:",
          binary_search(small_scores, existing_score))

    print("\nSearching for missing score:", missing_score)
    print("Linear search result:",
          linear_search(small_scores, missing_score))
    print("Binary search result:",
          binary_search(small_scores, missing_score))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # Create a sorted dataset containing values from 1 through 10,000.
    large_scores = list(range(1, 10001))
    large_target = 9999

    print("Searching a dataset containing 10,000 values.")
    print("Target value:", large_target)

    print("Linear search result:",
          linear_search(large_scores, large_target))
    print("Binary search result:",
          binary_search(large_scores, large_target))

    # Both algorithms find the same index, but linear search may check
    # thousands of values. Binary search repeatedly cuts the search
    # space in half, making it much more efficient for large sorted data.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list.
    # Neither algorithm can find the target, so both return -1.
    empty_scores = []

    print("\nEmpty list searching for 81:")
    print("Linear search result:",
          linear_search(empty_scores, 81))
    print("Binary search result:",
          binary_search(empty_scores, 81))

    # Edge Case 2: Single-element list.
    # The target is the only element, so both searches return index 0.
    single_score = [81]

    print("\nSingle-element list searching for 81:")
    print("Linear search result:",
          linear_search(single_score, 81))
    print("Binary search result:",
          binary_search(single_score, 81))


if __name__ == "__main__":
    main()
