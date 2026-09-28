# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compared Bubble Sort and Merge Sort. I implemented both sorting algorithms in Python and tested them using multiple datasets and edge cases.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. I tested Bubble Sort and Merge Sort using unsorted datasets.
2. I used multiple datasets with different values.
3. I demonstrated edge cases, including an empty list and a list containing duplicate values.
4. I compared the performance and behavior of Bubble Sort and Merge Sort.
5. I examined how sorting algorithms can be applied to real-world situations.

## Implementation Summary

I implemented Bubble Sort by creating a copy of the original list and repeatedly comparing adjacent values. When two values were out of order, they were swapped. I also used a `swapped` variable so the algorithm could stop early when no additional swaps were necessary.

I implemented Merge Sort using recursion and the divide-and-conquer approach. The original list was divided into smaller halves until each section contained one or zero elements. The `merge()` function then compared values from each half and combined them into a new sorted list.

Both algorithms successfully produced the same sorted results for the datasets that I tested.

## Edge Cases

I tested an empty list to verify that both algorithms could handle a dataset containing no values without producing an error.

I also tested a list containing duplicate values. Both sorting algorithms preserved all duplicate values and returned them in the correct sorted order.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and contrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to use each.
