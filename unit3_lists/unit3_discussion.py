"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):Maria Miller
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # Insert the new value at the requested index.
    # Elements at and after this position shift one place to the right.
    lst.insert(index, value)

    # Inserting near the beginning or middle can take more time because
    # several existing elements may need to move. Inserting at the end
    # usually requires less shifting.


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Check that the index is within the valid range before deleting.
    # This prevents the program from causing an IndexError.
    if 0 <= index < len(lst):
        return lst.pop(index)

    # Return None when the requested position does not exist.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search because each item is checked one at a time
    # from the beginning of the list until the value is found.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Return -1 when every item has been checked and no match was found.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Create a playlist containing several songs.
    playlist = ["Blinding Lights", "Levitating", "Flowers"]
    print("Original playlist:", playlist)

    # Insert a song at the beginning of the playlist.
    insert_at(playlist, 0, "Espresso")
    print("After inserting at the beginning:", playlist)

    # Insert a song into the middle of the playlist.
    middle_index = len(playlist) // 2
    insert_at(playlist, middle_index, "Die With A Smile")
    print("After inserting in the middle:", playlist)

    # Insert a song at the end using the current length as the index.
    insert_at(playlist, len(playlist), "Birds of a Feather")
    print("After inserting at the end:", playlist)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Remove the first song and display the removed value.
    removed = delete_at(playlist, 0)
    print("Removed from beginning:", removed)
    print("Updated playlist:", playlist)

    # Remove a song from the middle of the playlist.
    middle_index = len(playlist) // 2
    removed = delete_at(playlist, middle_index)
    print("Removed from middle:", removed)
    print("Updated playlist:", playlist)

    # Remove the final song using the last valid index.
    removed = delete_at(playlist, len(playlist) - 1)
    print("Removed from end:", removed)
    print("Updated playlist:", playlist)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for a song that still exists in the playlist.
    song = "Flowers"
    result = search_value(playlist, song)
    print(f"Search for '{song}': index {result}")

    # Search for a song that does not exist in the playlist.
    missing_song = "Shape of You"
    result = search_value(playlist, missing_song)
    print(f"Search for '{missing_song}': {result} (not found)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Try to delete from an index that does not exist.
    # The function safely returns None instead of causing an error.
    invalid_delete = delete_at(playlist, 100)
    print("Delete using invalid index:", invalid_delete)

    # Edge case 2: Try to delete from an empty list.
    # Since there are no valid indexes, the function returns None.
    empty_playlist = []
    empty_delete = delete_at(empty_playlist, 0)
    print("Delete from empty playlist:", empty_delete)

    # Edge case 3: Show that insertion also works with an empty list.
    insert_at(empty_playlist, 0, "New Song")
    print("Insert into empty playlist:", empty_playlist)

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    # A music playlist is a real-world example of a list because songs
    # can be added, removed, searched for, and kept in a specific order.
    print("\n=== REAL-WORLD SCENARIO ===")
    print("A music playlist uses a list to keep songs in a specific order.")


if __name__ == "__main__":
    main()
