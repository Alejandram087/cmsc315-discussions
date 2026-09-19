# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

## Implementation

I created an employee directory using a Python dictionary to demonstrate how dictionaries behave as hash tables. Employee IDs were used as keys, and employee names were stored as the corresponding values.

I inserted five employees into the dictionary and demonstrated lookup operations by retrieving employees using their IDs. I also updated an existing employee's name and deleted an employee from the dictionary.

To test edge cases, I attempted to look up an employee ID that did not exist by using the get() method. This returned a message instead of causing an error. I also checked whether an employee ID existed before attempting to delete it, which prevented an error when the key was not found.

This program demonstrated how dictionaries provide an efficient way to store, retrieve, update, and remove information using unique keys.
