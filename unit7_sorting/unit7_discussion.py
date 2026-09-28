"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Create a copy of the list so the original list is not changed.
    sorted_list = lst.copy()

    # Go through the list multiple times to move larger values to the end.
    for i in range(len(sorted_list) - 1):
        swapped = False

        # Compare adjacent elements in the list.
        for j in range(len(sorted_list) - 1 - i):
            if sorted_list[j] > sorted_list[j + 1]:
                # Swap the values if they are in the wrong order.
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )
                swapped = True

        # If no values were swapped, the list is already sorted.
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # A list with zero or one element is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle of the list.
    middle = len(lst) // 2

    # Divide the list into left and right halves.
    left_half = lst[:middle]
    right_half = lst[middle:]

    # Recursively sort each half.
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the two sorted halves and return the result.
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    # Create an empty list to store the merged result.
    result = []

    # Track the current position in each list.
    left_index = 0
    right_index = 0

    # Compare values from both lists until one list is exhausted.
    while left_index < len(left) and right_index < len(right):

        # Use <= so equal values from the left list stay first.
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining values from the left list.
    result.extend(left[left_index:])

    # Add any remaining values from the right list.
    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    # Create the first unsorted dataset with eight values.
    dataset1 = [42, 15, 8, 23, 4, 16, 35, 10]

    # Display the original dataset.
    print("Original List:", dataset1)

    # Sort Dataset #1 using both algorithms.
    print("Bubble Sort:", bubble_sort(dataset1))
    print("Merge Sort:", merge_sort(dataset1))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    # Create a second dataset using different values.
    dataset2 = [91, 27, 63, 12, 55, 38, 76, 19]

    # Display the original dataset.
    print("Original List:", dataset2)

    # Store the results from both sorting algorithms.
    bubble_result = bubble_sort(dataset2)
    merge_result = merge_sort(dataset2)

    # Display both sorted results.
    print("Bubble Sort:", bubble_result)
    print("Merge Sort:", merge_result)

    # Compare the results to verify both algorithms sorted the same way.
    print("Results Match:", bubble_result == merge_result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case #1: Empty list
    # An empty list contains no values, so both algorithms return an empty list.
    empty_list = []

    print("\nEmpty List:")
    print("Original:", empty_list)
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))
    print("Explanation: An empty list has no values to sort.")

    # Edge Case #2: List with duplicate values
    # Both algorithms should keep every duplicate while sorting the values.
    duplicate_list = [5, 2, 5, 1, 2, 8, 5]

    print("\nList With Duplicates:")
    print("Original:", duplicate_list)
    print("Bubble Sort:", bubble_sort(duplicate_list))
    print("Merge Sort:", merge_sort(duplicate_list))
    print(
        "Explanation: Both algorithms keep all duplicate values "
        "and place them in the correct sorted order."
    )


if __name__ == "__main__":
    main()
