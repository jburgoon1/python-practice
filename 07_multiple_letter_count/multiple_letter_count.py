def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # return {letter: letter.count(letter) for letter in phrase}
    letterCount = {}
    for letter in phrase:
        keys = letterCount.keys()
        if letter in keys:
            letterCount[letter]+=1
        else:
            letterCount[letter] = 1
    return letterCount
        
    