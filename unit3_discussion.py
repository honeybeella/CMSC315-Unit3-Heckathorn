

"""
==================================================
Unit 3 Discussion: List Operations
Insert, Delete, and Search
==================================================

This program demonstrates how Python lists behave when
items are inserted, deleted, and searched.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.
    """
    # The insert() method adds a value at the requested position.
    # Existing elements at that position and after it shift right.
    # Inserting at the beginning or middle may require shifting
    # multiple elements. Inserting at the end is usually faster.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.
    Return None if the index is invalid.
    """
    # Check whether the index exists before attempting deletion.
    # This prevents an IndexError if the list is empty or the
    # requested position is outside the valid range.
    if index < 0 or index >= len(lst):
        return None

    # pop() removes the item and returns its value.
    # Items after the removed item shift left to fill the gap.
    removed_value = lst.pop(index)
    return removed_value


def search_value(lst, value):
    """
    Return the index of a value or -1 if it is not found.
    """
    # This is a linear search because it checks list items
    # one at a time, starting from the beginning.
    # The search stops when it finds the requested value.
    # If the value is missing, every item must be checked.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    return -1


def main():
    print("=== UNIT 3: CAT CAFE LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================
    print("\n=== CAT ARRIVAL TESTS ===")

    cats = ["Luna", "Mochi", "Pumpkin", "Oreo"]
    print("Original list of cats:", cats)

    # Insert a new cat at the beginning of the list.
    insert_at(cats, 0, "Whiskers")
    print("After adding Whiskers at the beginning:", cats)

    # Insert a new cat in the middle of the list.
    middle_index = len(cats) // 2
    insert_at(cats, middle_index, "Cinnamon")
    print("After adding Cinnamon in the middle:", cats)

    # Insert a new cat at the end of the list.
    insert_at(cats, len(cats), "Cleo")
    print("After adding Cleo at the end:", cats)

    # ===============================
    # DELETION TESTS
    # ===============================
    print("\n=== CAT DEPARTURE TESTS ===")

    cafe_cats = ["Luna", "Mochi", "Pumpkin", "Oreo", "Cleo"]
    print("Original list of cats:", cafe_cats)

    # Remove the first cat from the list.
    removed_cat = delete_at(cafe_cats, 0)
    print("Cat removed from the beginning:", removed_cat)
    print("Updated list:", cafe_cats)

    # Remove a cat from the middle of the updated list.
    middle_index = len(cafe_cats) // 2
    removed_cat = delete_at(cafe_cats, middle_index)
    print("Cat removed from the middle:", removed_cat)
    print("Updated list:", cafe_cats)

    # Remove the last cat from the list.
    removed_cat = delete_at(cafe_cats, len(cafe_cats) - 1)
    print("Cat removed from the end:", removed_cat)
    print("Updated list:", cafe_cats)

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== FIND A CAT ===")

    available_cats = ["Luna", "Mochi", "Pumpkin", "Oreo"]
    print("Cats currently available:", available_cats)

    # Search for a cat that is in the list.
    result = search_value(available_cats, "Pumpkin")
    print("Searching for Pumpkin:", result)

    # Search for a cat that is not in the list.
    result = search_value(available_cats, "Fluffy")
    print("Searching for Fluffy:", result)

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== CAT LIST EDGE CASES ===")

    # Edge case 1: Add a cat to an empty list.
    empty_cat_list = []
    print("Starting with an empty cat list:", empty_cat_list)

    insert_at(empty_cat_list, 0, "Baby Cat")
    print("After adding Baby Cat:", empty_cat_list)

    # Edge case 2: Try deleting a cat using an invalid index.
    invalid_result = delete_at(available_cats, 10)
    print("Attempt to remove a cat at invalid index 10:", invalid_result)
    print("Cat list remains unchanged:", available_cats)

    # Edge case 3: Search for a cat that does not exist.
    missing_cat = search_value(available_cats, "Fluffy")
    print("Search result for Fluffy:", missing_cat)

    # Edge case 4: Try deleting a cat from an empty list.
    empty_delete = delete_at([], 0)
    print("Attempt to remove a cat from an empty list:", empty_delete)

    # Edge case 5: Delete the only cat in a one-item list.
    one_cat_list = ["Tiny"]
    print("List with only one cat:", one_cat_list)

    removed_cat = delete_at(one_cat_list, 0)
    print("Removed the only cat:", removed_cat)
    print("List after deletion:", one_cat_list)

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================
    print("\n=== REAL-WORLD CAT CAFE SCENARIO ===")

    # A cat cafe tracks cats that are available for adoption.
    adoption_cats = ["Luna", "Mochi", "Pumpkin"]
    print("Cats available for adoption:", adoption_cats)

    # A new cat arrives at the cafe.
    insert_at(adoption_cats, len(adoption_cats), "Whiskers")
    print("After Whiskers arrives:", adoption_cats)

    # Mochi gets adopted, so the cafe removes Mochi from the list.
    cat_index = search_value(adoption_cats, "Mochi")

    if cat_index != -1:
        adopted_cat = delete_at(adoption_cats, cat_index)
        print(adopted_cat, "has been adopted!")

    print("Cats still available for adoption:", adoption_cats)

    # Check whether Luna is still available.
    cat_index = search_value(adoption_cats, "Luna")

    if cat_index != -1:
        print("Luna is still waiting for a home!")
    else:
        print("Luna is no longer on the adoption list.")

    print("\n=== CAT CAFE PROGRAM COMPLETE ===")


if __name__ == "__main__":
    main()

