def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    newList = []
    for item in lst:
        if isinstance(item, list):
            newList.append(item)
    print(newList)
    if len(newList)== len(lst):
        return True
    else:
        return False