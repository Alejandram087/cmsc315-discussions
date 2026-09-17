# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compared linear search and binary search. I implemented both
algorithms in Python and tested them using small and large sorted datasets. I
also tested edge cases to observe how each algorithm handled unusual inputs.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Tested both algorithms on a small dataset.
2. Tested both algorithms on a large dataset.
3. Demonstrated edge cases.
4. Analyzed performance.
5. Created a real-world search scenario using student scores.

## Implementation

I implemented a linear search that checked each value in the list from
beginning to end until the target was found. The method returned the index
when the target existed and returned -1 when it was not found.

I also implemented a binary search for sorted data. The algorithm calculated
the middle index and eliminated half of the remaining search area after each
comparison. It continued until the target was found or there were no values
left to search.

For the real-world scenario, I used student scores. I tested an existing score
and a score that was not present. I also used a dataset containing 10,000
values to demonstrate how binary search became more efficient as the dataset
increased in size.

## Edge Cases

I tested an empty list and a single-element list. When an empty list was
searched, both algorithms returned -1 because there were no values available
to search. When a single-element list containing the target value was
searched, both algorithms successfully returned index 0.

## Performance Analysis

Linear search had O(n) time complexity because, in the worst case, it had to
check every element in the list. Binary search had O(log n) time complexity
because each comparison eliminated approximately half of the remaining search
space.

Binary search was more efficient for large sorted datasets. However, linear
search remained useful when data was unsorted or when the dataset was small
enough that sorting it first would not provide a meaningful benefit.

## Discussion Board Reflection

While completing this assignment, I learned more about how linear search and
binary search locate values and how the organization of data affects algorithm
performance. Implementing linear search was straightforward because I checked
each element from the beginning of the list until the target was found.
Binary search required more attention because I had to track the low, high,
and middle positions while reducing the search area after each comparison.

One challenge was making sure binary search correctly updated its boundaries
without skipping possible values. Testing an empty list and a single-element
list helped me verify that the algorithm also handled edge cases correctly.

Linear search is useful for small or unsorted datasets because it does not
require the data to be organized beforehand. Binary search is much faster for
large sorted datasets because it eliminates approximately half of the
remaining values after every comparison. However, binary search cannot be
used directly on unsorted data. In a real-world application, I would consider
whether the time required to sort the data was worthwhile before choosing
binary search.
