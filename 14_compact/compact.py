def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    falsy = ['',[],False,(),None,]
    newList = []
    goodList = []
    for item in lst:
        if item in falsy:
            idx = lst.index(item)
            newList.append(lst[idx:idx+1])
        else:
            goodList.append(item)
    return goodList
        