def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    #  - lists/strings/sets/tuples: returns True/False if sought present
    # - dictionaries: return True/False if *value* of sought in dictionary

    if isinstance(collection, list):
        if start:
            new_list = collection[start:]
            for item in new_list:
                if item == sought:
                    return True
                else:
                    return False
        else:
            for item in collection:
                if item == sought:
                    return True
                else:
                    return False
    elif isinstance(collection, str):
            if start:
                new_str = collection[start:]
                # print(new_str)
                for item in new_str:
                    # print(f"item={item}")
                    # print(f"sought={sought}")
                    if item == sought:
                        return True
                return False
            else:
                if collection.find(sought) == -1:
                    return False
                else:
                    return True
    elif isinstance(collection, set):
        return sought in collection
    elif isinstance(collection, tuple):
        if start:
                new_tup = collection[start:]
                # print(new_tup)
                for item in new_tup:
                    if item == sought:
                        return True
                return False
        else:
            if collection.find(sought) == -1:
                return False
            else:
                return True
    elif isinstance(collection, dict):
        for item in collection.values():
            if item == sought:
                return True
        return False
