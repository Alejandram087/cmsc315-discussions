"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # Create an empty dictionary for an employee directory.
    # Python dictionaries behave like hash tables by using
    # keys to quickly locate their associated values.
    employees = {}

    # Add employee IDs as keys and employee names as values.
    employees[1001] = "Maria"
    employees[1002] = "John"
    employees[1003] = "Sarah"
    employees[1004] = "David"
    employees[1005] = "Emily"

    print("Employee directory:", employees)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # A dictionary uses the key to find its associated value.
    # Here, the employee ID is used to retrieve the employee name.
    print("Employee 1002:", employees[1002])
    print("Employee 1004:", employees[1004])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:", employees)

    # Assigning a new value to an existing key replaces
    # the previous value instead of creating a duplicate key.
    employees[1003] = "Sarah Johnson"

    print("After update:", employees)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:", employees)

    # Removing a key also removes the value associated with it.
    del employees[1005]

    print("After deletion:", employees)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Use get() to safely search for a missing employee.
    # This avoids an error if the key does not exist.
    missing_employee = employees.get(9999, "Employee not found")
    print("Lookup employee 9999:", missing_employee)

    # Edge case 2: Check whether a key exists before deleting it.
    # This prevents an error when attempting to delete a missing key.
    employee_to_delete = 2000

    if employee_to_delete in employees:
        del employees[employee_to_delete]
        print("Employee deleted.")
    else:
        print("Employee 2000 cannot be deleted because the ID was not found.")

    print("\nFinal employee directory:", employees)


if __name__ == "__main__":
    main()
