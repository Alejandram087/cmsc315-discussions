# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compared Bubble Sort and Merge Sort. I implemented both sorting algorithms in Python and tested them using multiple datasets and edge cases.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort using unsorted datasets.
2. Use multiple datasets with different values.
3. Demonstrate edge cases, including an empty list and a list containing duplicate values.
4. Compare the performance and behavior of Bubble Sort and Merge Sort.
5. Examine how sorting algorithms can be applied to real-world situations.

## Implementation Summary

I implemented Bubble Sort by creating a copy of the original list and repeatedly comparing adjacent values. When two values were out of order, they were swapped. I also used a `swapped` variable so the algorithm could stop early when no additional swaps were necessary.

I implemented Merge Sort using recursion and the divide-and-conquer approach. The original list was divided into smaller halves until each section contained one or zero elements. The `merge()` function then compared values from each half and combined them into a new sorted list.

Both algorithms successfully produced the same sorted results for the datasets that I tested.

## Edge Cases

I tested an empty list to verify that both algorithms could handle a dataset containing no values without producing an error.

I also tested a list containing duplicate values. Both sorting algorithms preserved all duplicate values and returned them in the correct sorted order.

