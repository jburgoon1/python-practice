def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowelCount = {}
    vowel = 'aeiou'
    for letter in phrase.lower():
        if letter in vowel:
            key = vowelCount.keys()
            if letter in key:
                vowelCount[letter]+=1
            else:
                vowelCount[letter]=1
    return vowelCount
